#!/usr/bin/node
/* a class Rectangle that defines a rectangle */
class Rectangle {
  constructor(w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    } else {
    
     
    }
  }
}

module.exports = Rectangle;
