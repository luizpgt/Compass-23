const express = require('express');
const exphbs = require('express-handlebars');
const path = require('path');
const app = express();
const PORT = 3000;
const comic = require('./routes/xkcdPlusGiphy');

// Configure handlebars
app.set('views', path.join(__dirname, 'views'));
app.engine('handlebars', exphbs.engine({ defaultLayout: 'main' }));
app.set('view engine', 'handlebars');

// Define routes

// Redirect the root route to the '/comic' route
app.get('/', (req, res) => res.redirect('/comic'));

// Route to handle filtering by ID
app.get('/filter', (req,res) => {
  try {
    let id = parseInt(req.query.id);
    res.redirect(`/comic/id/${id}`);
  } catch (error) {
    console.error(error);
    res.redirect('/');
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});

// Route handlers
app.use('/comic', comic.router);