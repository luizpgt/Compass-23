const MediaItem = require('./MediaItem');

class Comic extends MediaItem {
  constructor(id, url, title, description) {
    super(id, url, title);
    this.description = description;
    this.prev = id - 1;
    this.next = id + 1;
  }
}

module.exports = Comic;
