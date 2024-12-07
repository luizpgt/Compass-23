const express = require('express');
const router = express.Router();
const xkcdController = require('../controllers/xkcdController');
const giphyController = require('../controllers/giphyController');

/**
 * Method: GET
 * Renders the index view with a random comic and corresponding GIFs.
 */

router.get('/', async (req, res) => {
    comicData = await xkcdController.getRandomComic();
    giphyData = await giphyController.getGifs(comicData.title);
    res.render('index', { wcomic: comicData, gifs: giphyData });
});


/**
 * Method: GET
 * Renders the index view with the comic and corresponding GIFs for the specified ID.
 * If the ID is invalid, redirects to the random comic route.
 */

router.get('/id/:id', async (req, res) => {
    comicData = await xkcdController.getComicById(req.params.id);
    if (comicData) { // se id_escolhido > max_id : manda pra rota random 
        giphyData = await giphyController.getGifs(comicData.title);
        res.render('index', { wcomic: comicData, gifs: giphyData });
    } else {
        res.redirect('/');
    }
});

/**
 * Method: GET
 * Renders the index view with the last comic and corresponding GIFs.
 */

router.get('/last', async (req, res) => {
    comicData = await xkcdController.getLastComic();
    giphyData = await giphyController.getGifs(comicData.title);
    res.render('index', { wcomic: comicData, gifs: giphyData });
});


module.exports = {router};