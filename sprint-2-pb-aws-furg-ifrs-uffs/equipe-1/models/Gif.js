const MediaItem = require('./MediaItem');

class Gif extends MediaItem {
  constructor(id, url, title) {
    super(id, url, title);
  }
}

module.exports = Gif;
