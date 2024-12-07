const axios = require('axios');
const Gif = require('../models/Gif');

// if giphy's api key is not available, runs the program anyways with just the comic
let giphyApiKey = 0;
try {
    const config = require('../config');
    if (config.giphyApiKey)
        giphyApiKey = config.giphyApiKey;
    else throw Error;
} catch (error) {
    console.error('[Giphy key not found]: Please check if config.js exists on project\'s root folder and exports a valid \"giphyApiKey\"!');
}

/**
 * Retrieves GIFs (Array of Gifs) related to the given comic title.
 */
async function getGifs(comicTitle, limit = 2) {
    try {
        if (!giphyApiKey)
            return;
        const url = `https://api.giphy.com/v1/gifs/search?api_key=${giphyApiKey}&limit=${limit}&q=${comicTitle}`;
        const response = await axios.get(url);
        const gifData = response.data;
        const gifs = gifData.data.map(gif => {
            const { id, title } = gif;
            const url = gif.images.downsized.url;
            return new Gif(id, url, title);
        });
        return gifs;
    } catch (error) {
        console.error(error);
    }
}

module.exports = {getGifs};