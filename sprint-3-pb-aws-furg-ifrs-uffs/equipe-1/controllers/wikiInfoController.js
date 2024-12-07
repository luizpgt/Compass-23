const axios = require('axios');
const WikiInfo = require('../models/WikiInfo');

/**
 * Creates a Comic object from the retrieved data.
 */
function retrieveData (data) {

    const {title, description} = data;
    const thumbnailUrl = 'https:' + data.thumbnail.url;
    return new WikiInfo(title, description, thumbnailUrl);
}
/**
 * Retrieves info about the author related to the given author's name : from mediawiki api.
 */
async function getAuthorInfo(author) {
    try {
        const url = `https://en.wikipedia.org/w/rest.php/v1/search/page?q=${author + ' stoic philosopher'}&limit=1`;
        const response = await axios.get(url);
        return retrieveData(response.data.pages[0]);
    } catch (error) {
        console.error(error);
    }
}

module.exports = { getAuthorInfo };