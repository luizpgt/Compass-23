const { v4: uuidv4 } = require('uuid')

/**
 * Converts a date string from YYYY-MM-DD format to DD-MMMM-YYYYY format.
 *
 * @param {string} strDate - The input date string in YYYY-MM-DD format.
 * @returns {string} The converted date string in DD-MM-YYYY format.
 */
function stringYmdToDmy(strDate) {
  return strDate.split('-').reverse().join('-')
}


/**
 * Create a unique id.
 * 
 * @returns {string} A id string in XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX format.
 */
function generateRandomId() {
  return uuidv4()
}
module.exports = { stringYmdToDmy, generateRandomId }