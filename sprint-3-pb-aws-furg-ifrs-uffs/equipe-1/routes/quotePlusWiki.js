const express = require('express');
const router = express.Router();
const quoteController = require('../controllers/quoteController');
const wikiInfoController = require('../controllers/wikiInfoController');

/**
 * Method: GET
 * Renders the index view with a random quote and corresponding Wiki info.
 */

router.get('/', async (req, res) => {
    quoteData = await quoteController.getRandomQuote();
    if(!quoteData) return;
    authorData = await wikiInfoController.getAuthorInfo(quoteData.author);
    res.render('index', {quote: quoteData, author: authorData});
});

/**
 * Method: GET
 * Renders the index view with the quote and corresponding Wiki info for the specified ID.
 * If the ID is invalid, redirects to the random quote route.
 */

router.get('/id/:id', async (req, res) => {
    try{
        let id = parseInt(req.params.id);
        quoteData = await quoteController.getQuoteById(id);
        if (!quoteData) return;
        authorData = await wikiInfoController.getAuthorInfo(quoteData.author);
        res.render('index', {quote: quoteData, author: authorData});
    } catch(error){
        res.redirect('/')
    }
    
});

module.exports = {router};