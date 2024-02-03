const ctx = document.getElementById("output").getContext('2d');
const screenWidth = 500;
const screenHeight = 500;

document.getElementById("output").width = screenWidth;
document.getElementById("output").height = screenHeight;

// one value for each pixel in our screen
const depthBuffer = new Array(screenWidth * screenHeight);

// create buffer for color output
const numChannels = 3; // R G B
const colorBuffer = new Array(screenWidth * screenHeight * numChannels);

/**
 * Represents a 2D box
 * @class
 */
class Box {
  /** @member {Object} position of the box storing x,y,z coordinates */
  position;
  /** @member {Object} size of the box storing width and height */
  size;
  /** @member {Object} color of the box given in RGB */
  color;

  constructor (props) {
    this.position = props.position;
    this.size = props.size;
    this.color = props.color;
  }

  /**
   * Check if given point is in box
   * @param {Number} px coordinate of the point
   * @param {Number} py coordinate of the point
   * @return {Boolean} point in box
   */
  pointInBox (px,py) {
    return this.position.x < px && this.position.x + this.size.width > px
        && this.position.y < py && this.position.y + this.size.height > py;
  }
}

const boxes = [
  // red box
  new Box({
    position: { x: 50, y: 50, z: 10 },
    size: { width: 150, height: 50 },
    color: { r: 255, g: 0, b:0 }
  }),
  // green box
  new Box({
    position: { x: 80, y: 30, z: 5 },
    size: { width: 10, height: 150 },
    color: { r: 0, g: 255, b:0 }
  }),
  // blue
  new Box({
    position: { x: 70, y: 70, z: 8 },
    size: { width: 50, height: 40 },
    color: { r: 0, g: 0, b: 255 }
  }),
  new Box({
    position: { x: 70, y: 70, z: 8 },
    size: { width: 50, height: 40 },
    color: { r: 0, g: 0, b: 255 }
  })
];

const varyZ = document.getElementById('varyz');
varyZ.onchange = draw;
function draw () {
  // clear depth buffer of previous frame
  depthBuffer.fill(10);
  for(const box of boxes) {
    for(let x = 0; x < screenWidth; x++) {
      for(let y = 0; y < screenHeight; y++) {
        // check if our pixel is within the box
        if (box.pointInBox(x,y)) {
          // check if this pixel of our box is covered by something else
          // compare depth value in depthbuffer against box position
          if (depthBuffer[x + y * screenWidth] < box.position.z) {
            // something is already closer to the viewpoint that our current primitive, don't draw this pixel:
            if (!varyZ.checked) continue;
            if (depthBuffer[x + y * screenWidth] < box.position.z + Math.sin((x+y))*Math.cos(x)*5) continue;
          }
          // we passed the depth test, put our current depth value in the z-buffer
          depthBuffer[x + y * screenWidth] = box.position.z;
          // put the color in the color buffer, channel by channel
          colorBuffer[(x + y * screenWidth)*numChannels + 0] = box.color.r;
          colorBuffer[(x + y * screenWidth)*numChannels + 1] = box.color.g;
          colorBuffer[(x + y * screenWidth)*numChannels + 2] = box.color.b;
        }
      }
    }
  }

  // convert to rgba for presentation
  const oBuffer = new Uint8ClampedArray(screenWidth*screenHeight*4);
  for (let i=0,o=0; i < colorBuffer.length; i+=3,o+=4) {
  oBuffer[o]=colorBuffer[i];
  oBuffer[o+1]=colorBuffer[i+1];
  oBuffer[o+2]=colorBuffer[i+2];
  oBuffer[o+3]=255;
  }
  ctx.putImageData(new ImageData(oBuffer, screenWidth, screenHeight),0,0);
}

document.getElementById('redz').oninput = e=>{boxes[0].position.z=parseInt(e.target.value,10);draw()};
document.getElementById('greenz').oninput = e=>{boxes[1].position.z=parseInt(e.target.value,10);draw()};
document.getElementById('bluez').oninput = e=>{boxes[2].position.z=parseInt(e.target.value,10);draw()};

draw();