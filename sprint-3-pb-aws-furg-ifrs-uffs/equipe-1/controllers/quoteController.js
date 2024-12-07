const axios = require('axios');
const Quote = require('../models/Quote');

const maxId = 402;

async function getQuoteById(id) {
    try {
        const reqConfig = {
            data: {
                id: assureValidId(id)
            }
        }
        return axios
        .get('https://stoic-api.vercel.app/api/quote', reqConfig)
        .then(response => {
            return retrieveData(response.data.data);})
        .catch(function (error) {
        if (error.response) {
          console.log("Foram feitas muitas requisições! Por favor, espere até fazer uma próxima!");
          return null;
        };}
        );
    } catch (error) {
        console.error(error);
        return null;
    }
}

/**
 * Creates a Quote object from the retrieved data.
 */
function retrieveData (data) {
    const { id, author, quote, source } = data;
    const quoteData = new Quote(id, author, quote, source);
    return quoteData;
}

/**
 * Retrieves a random Quote
 */
async function getRandomQuote() {
    const randomId = Math.floor(Math.random() * maxId) + 1;
    return getQuoteById(randomId);
}


/**
 * Calculates the Quote ID based on the last Quote and the current Quote.
 */
function assureValidId(id) {
    return id%(maxId+1);
}

module.exports = { getRandomQuote, getQuoteById };