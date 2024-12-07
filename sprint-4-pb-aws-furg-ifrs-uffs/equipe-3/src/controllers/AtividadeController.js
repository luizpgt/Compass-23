require('dotenv').config()

const axios = require('axios')
const { generateRandomId } = require('../utils/helper')
const Atividade = require('./../models/Atividade')

/**
 * Make request to BORED_API_ACTIVITIES and returns
 * the API's json response
 * 
 * @returns {Object|null} - The API's JSON response if successful, or null in case of an error.
 */
async function fetchAtividadeData() {
  try {
    const BORED_API_URL = process.env.BORED_API_URL
    const { data } = await axios.get(BORED_API_URL)
    if (data.error) {
      throw new Error(data.error)
    }
    return data
  } catch (error) {
    return null
  }
}

/**
 * Returns an Atividade Object with data 
 * fed from json argument
 * 
 * @param {Object} data - The JSON data containing details for creating the Atividade object
 * @returns {Atividade|null} - An instance of the Atividade class with extracted data,
 *                            or null if no data is provided.
 */
function formatAtividadeData(data) {

  if (!data) return null
  const id = generateRandomId()
  const accessibility = formatAccessibility(data.accessibility)
  const { activity, type, participants } = data

  return new Atividade(id, activity, type, participants, accessibility)
}

/**
 * Formats an accessibility value as a percentage string.
 *
 * @param {number} accessibility - The accessibility value to be formatted (assumed as a decimal).
 * @returns {string} - The formatted accessibility value as a percentage string.
 */
function formatAccessibility(accessibility) {
  return `${(accessibility * 100).toFixed(0)}%`;
}

module.exports = { fetchAtividadeData, formatAtividadeData, formatAccessibility }