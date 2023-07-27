import secret_key_decorator from '../local_settings.js'

export default {
  delimiters: ["{$", "$}"],
  data() {
    return {
      titulo: "Hola, este es mi título",
    };
  },
  template: await extraeUrl(urlHtmlComponente).then(resp => { return resp })
}

async function extraeUrl(url) {
  let respuesta = await axios.get(url, {
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'X-MyApp-Secret-Key': secret_key_decorator
  }
  })
  let external_template = await respuesta.data
  return external_template
}