//ssl configurations
var fs = require('fs');
var http = require('http');
var https = require('https');

const privateKey = fs.readFileSync('/etc/letsencrypt/live/peptipedia.cl/privkey.pem', 'utf8');
const certificate = fs.readFileSync('/etc/letsencrypt/live/peptipedia.cl/cert.pem', 'utf8');
const ca = fs.readFileSync('/etc/letsencrypt/live/peptipedia.cl/chain.pem', 'utf8');

const credentials = {key: privateKey, cert: certificate, ca: ca};

const express = require('express'); //app se ejecutara en index.js
const path = require('path');
const exphbs = require('express-handlebars');
//const { DH_NOT_SUITABLE_GENERATOR } = require('constants');

//initializations
const app = express();

//settings
app.set('port', 80);
app.set('views', path.join(__dirname, 'views'));//donde esta la carpeta views
app.engine('.hbs', exphbs({ 
    // layouts plantilla que tiene codigo comun como el nav o footer y desde otro archivo se llama
    // partials pedazos de codigos para importar en otros archivos
    // estos archivos se crearan en views
    defaultLayout: 'main',
    layoutsDir: path.join(app.get('views'), 'layouts'), //directorio de layouts
    partialsDir: path.join(app.get('views'), 'partials'), //directorio de partials
    extname: '.hbs', //extencion de los archivos de views
    //custom helpers
    helpers: {
        calculation: function(name_value, name, value){
            if (name_value == name){
                return value;
            }
        },
        calculation_matrix: function(name, value, indice){
            activities = ['Propeptide', 'Signal', 'Transit', 'Sensorial', 'Drug delivery vehicle', 'Therapeutic', 'Other activity', 'Neurological activity', 'Immunological activity', 'non_activity']
            for (let index = 0; index < activities.length; index++) {
                if (name == activities[index]){
                    return value[indice];
                }
            }
        },
        calculation_matrix_id: function(value, index){
                return value[index];
        },
        matrix: function(name, value){
            activities = ['Propeptide', 'Signal', 'Transit', 'Sensorial', 'Drug delivery vehicle', 'Therapeutic', 'Other activity', 'Neurological activity', 'Immunological activity', 'non_activity']
            for (let index = 0; index < activities.length; index++) {
                if (name == activities[index]){
                    return value;
                }
            }
        },
        tree: function(name, value){
                if (name == "1"){
                    return value;
                }else{
                    return false
                }
        },
        found_in: function(name){
                if (name == "1"){
                    return "✔";
                }else{
                    return "Not found"
                }
        },
        codes: function(name){
                if (name == "0"){
                    return "Not Found";
                }else{
                    return name;
                }
        },
        test: function(name){
            return name
        }
    }
}))
app.set('view engine', '.hbs'); //setear lo configurado

//middlewares
app.use(express.urlencoded({extended: false})); //cada vez que llegue un dato de un form se convertira en un json

//routes
app.use(require('./routes/routes'));//requerimos el archivo de rutas de index

//static files
app.use(express.static(path.join(__dirname, 'public')));

const httpServer = http.createServer(app);
const httpsServer = https.createServer(credentials, app);

httpServer.listen(8080);
httpsServer.listen(8443);

module.exports = app; //exportamos para requerirlo de otro lado
module.exports = httpServer;
module.exports = httpsServer;

