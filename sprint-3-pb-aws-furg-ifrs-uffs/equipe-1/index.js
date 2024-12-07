const express = require('express');
const exphbs = require('express-handlebars');
const path = require('path');
const app = express();
const PORT = 3000;
const quote = require('./routes/quotePlusWiki');

// Configure handlebars
app.set('views', path.join(__dirname, 'views'));
app.engine('handlebars', exphbs.engine({ defaultLayout: 'main' }));
app.set('view engine', 'handlebars');

// Define routes

// Redirect the root route to the '/quote' route
app.get('/', (req, res) => res.redirect('/quote'));


// Start server
app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});

// Route handlers
app.use('/quote', quote.router);