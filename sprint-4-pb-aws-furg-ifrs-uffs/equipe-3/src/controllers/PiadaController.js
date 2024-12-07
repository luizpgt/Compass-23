require('dotenv').config()

const axios = require('axios')
const { generateRandomId } = require('../utils/helper')
const { stringYmdToDmy } = require('../utils/helper')
const Piada = require('./../models/Piada')
/**
 * Make request to CHUCK_NORRIS_API and returns
 * the API's json response
 * 
 * @returns {Object|null} - The API's JSON response if successful, or null in case of an error.
 */
async function fetchPiadaData() {
  try {
    const CHUCK_NORRIS_API_URL = process.env.CHUCK_NORRIS_API_URL
    const { data } = await axios.get(CHUCK_NORRIS_API_URL)
    if (data.error) {
      throw new Error(data.error)
    }
    return data
  } catch (error) {
    return null
  }
}

/**
 * Returns a Piada Object with data 
 * fed from json argument
 * 
 * @param {Object} data - The JSON data containing details for creating the Piada object
 * @returns {Piada|null} - An instance of the Piada class with extracted data,
 *                            or null if no data is provided.
 */
function formatPiadaData(data) {
  const id = generateRandomId()
  const { icon_url, url } = data
  /* data.(created|updated)_at[0] == yyyy-mm-dd */
  const created_at = stringYmdToDmy(data.created_at.split(' ')[0])
  const updated_at = stringYmdToDmy(data.updated_at.split(' ')[0])
  const value = data.value.replace(/Chuck Norris/gi, 'CHUCK NORRIS')

  return new Piada(updated_at, created_at, icon_url, id, value, url)
}

module.exports = { fetchPiadaData, formatPiadaData }
