const fs = require('fs');
const http = require('http');
const indexCtrl = {};
const Peptide = require('../models/Peptide'); //modelo de base de datos
const Statistic = require('../models/Statistic');
const Activity = require('../models/Activity');
const Organism = require('../models/Organism');
const rimraf = require("rimraf");
var multer = require("multer");
var url = require('url');
const { response } = require('express');

indexCtrl.renderIndex = async(req,res) =>{ //ruta de index
    const statistics_full = await Statistic.find({$and:[{'Name': {$ne : "Total number of records"}},{'Name': {$ne : "Total number of organism"}},{'Name': {$ne : "Total PDB codes"}},{'Name': {$ne : "Histogram1"}},{'Name': {$ne : "PieChart1"}},{'Name': {$ne : "Total Uniprot codes"}},{'Name': {$ne : "Glossary"}}]}).lean();
    res.render('index', {statistics_full});
};
indexCtrl.renderAbout = (req,res) =>{ //ruta de about
    res.render('about');
};
indexCtrl.renderDatabase = async(req,res) =>{ //ruta de about
    const statistics = await Statistic.find().lean();
    const activities = await Statistic.find({$and:[{'Name': {$ne : "Total number of records"}},{'Name': {$ne : "Total number of organism"}},{'Name': {$ne : "Total PDB codes"}},{'Name': {$ne : "Histogram1"}},{'Name': {$ne : "PieChart1"}},{'Name': {$ne : "Total Uniprot codes"}},{'Name': {$ne : "Glossary"}}]}).lean();
    res.render('database', {statistics, activities});
};
indexCtrl.renderSearch = async(req,res) =>{ //ruta de about
    const organisms = await Organism.find({}).lean();
    res.render('search', {organisms});
};
indexCtrl.renderTools = (req,res) =>{ //ruta de about
    res.render('tools');
};
indexCtrl.renderDetails = async(req,res) =>{ //ruta de about
    if (req.params.id == 'Propeptide' || 
    req.params.id == 'Signal' || 
    req.params.id == 'Transit' ||
    req.params.id == 'Sensorial' ||
    req.params.id == 'Drugdeliveryvehicle' ||
    req.params.id == 'Therapeutic' ||
    req.params.id == 'Otheractivity' ||
    req.params.id == 'Neurologicalactivity' ||
    req.params.id == 'Immunologicalactivity' ||
    req.params.id == 'non_activity'
    ){
        if(req.params.id == 'Drugdeliveryvehicle'){
            req.params.id = 'Drug delivery vehicle'
        }
        if(req.params.id == 'Otheractivity'){
            req.params.id = 'Other activity'
        }
        if(req.params.id == 'Neurologicalactivity'){
            req.params.id = 'Neurological activity'
        }
        if(req.params.id == 'Immunologicalactivity'){
            req.params.id = 'Immunological activity'
        }
        const statistics = await Statistic.find({"Name": req.params.id}).lean();
        const statistics_full = await Statistic.find({$and:[{'Name': {$ne : "Total number of records"}},{'Name': {$ne : "Total number of organism"}},{'Name': {$ne : "Total PDB codes"}},{'Name': {$ne : "Histogram1"}},{'Name': {$ne : "PieChart1"}},{'Name': {$ne : "Total Uniprot codes"}},{'Name': {$ne : "Glossary"}}]}).lean();
        res.render('details', {statistics, statistics_full});
    }else{
        res.redirect('../');
    }
};
indexCtrl.getDatabase = async(req, res) =>{
    const peptides = await Peptide.find().lean(); //buscamos todas las notas y las traemos en json
    res.send(peptides);
}
indexCtrl.getDatabasePerActivity = async(req, res) =>{
    const activities = await Activity.find({"activity": req.params.id}).lean(); //buscamos todas las notas y las traemos en json
    res.send(activities);   
}

indexCtrl.getSearch = async(req, res) =>{
    if (typeof req.body['organisms[]'] === 'string' || req.body['organisms[]'] instanceof String){
        req.body['organisms[]'] = [req.body['organisms[]']]
    }

    all_activities = []
    if (!Array.isArray(req.body['activity_lvl_1[]'])){
        if (req.body['activity_lvl_1[]'] != undefined){
            all_activities.push(req.body['activity_lvl_1[]']);
        }
    }
    if (Array.isArray(req.body['activity_lvl_1[]'])){
        all_activities = all_activities.concat(req.body['activity_lvl_1[]']);
    }
    if (!Array.isArray(req.body['activity_lvl_2[]'])){
        if (req.body['activity_lvl_2[]'] != undefined){
            all_activities.push(req.body['activity_lvl_2[]']);
        }
    }
    if (Array.isArray(req.body['activity_lvl_2[]'])){
        all_activities = all_activities.concat(req.body['activity_lvl_2[]']);
    }
    if (!Array.isArray(req.body['activity_lvl_3[]'])){
        if (req.body['activity_lvl_3[]'] != undefined){
            all_activities.push(req.body['activity_lvl_3[]']);
        }
    }
    if (Array.isArray(req.body['activity_lvl_3[]'])){
        all_activities = all_activities.concat(req.body['activity_lvl_3[]']);
    }
    if (!Array.isArray(req.body['activity_lvl_4[]'])){
        if (req.body['activity_lvl_4[]'] != undefined){
            all_activities.push(req.body['activity_lvl_4[]']);
        }
    }
    if (Array.isArray(req.body['activity_lvl_4[]'])){
        all_activities = all_activities.concat(req.body['activity_lvl_4[]']);
    }
    if (!Array.isArray(req.body['activity_lvl_5[]'])){
        if (req.body['activity_lvl_5[]'] != undefined){
            all_activities.push(req.body['activity_lvl_5[]']);
        }
    }
    if (Array.isArray(req.body['activity_lvl_5[]'])){
        all_activities = all_activities.concat(req.body['activity_lvl_5[]']);
    }
    for (let index = 0; index < all_activities.length; index++) {
        if (all_activities[index] == 'Quorum sensing' || all_activities[index] == 'Chemotactic' || all_activities[index] == 'Cell-cell communication' || all_activities[index] == 'Defense'){    
            var flag = all_activities.indexOf('Sensorial');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Cell-penetrating' || all_activities[index] == "Blood-brain barrier crossing"){    
            var flag = all_activities.indexOf('Drug delivery vehicle');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Antimicrobial' || all_activities[index] == "Toxic" || all_activities[index] == "Metabolic" || all_activities[index] == "Anticancer" || all_activities[index] == "Bioactive"){    
            var flag = all_activities.indexOf('Therapeutic');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Cancer cell' || all_activities[index] == "Mammallian cell" || all_activities[index] == "Proteolytic" || all_activities[index] == "Surface-immobilized"){    
            var flag = all_activities.indexOf('Other activity');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Neuropeptide' || all_activities[index] == "Antinociceptive" || all_activities[index] == "Brain peptide"){    
            var flag = all_activities.indexOf('Neurological activity');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Allergen' || all_activities[index] == 'Immunomodulatory'){    
            var flag = all_activities.indexOf('Immunological activity');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Antiviral' || all_activities[index] == 'Antibacterial/antibiotic' || all_activities[index] == 'Antifungal' || all_activities[index] == 'Antiprotozoal' || all_activities[index] == 'Anuro defense'){    
            var flag = all_activities.indexOf('Antimicrobial');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Antiparasitic' || all_activities[index] == 'Cytolytic' || all_activities[index] == 'Insecticidal'){    
            var flag = all_activities.indexOf('Toxic');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Antihypertensive' || all_activities[index] == 'Anti Diabetic' || all_activities[index] == 'Antiinflammatory' || all_activities[index] == 'Enzyme inhibitor' || all_activities[index] == 'Regulatory' || all_activities[index] == 'Anti Angiogenic'){    
            var flag = all_activities.indexOf('Metabolic');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Antitumour'){    
            var flag = all_activities.indexOf('Anticancer');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Antioxidant'){    
            var flag = all_activities.indexOf('Bioactive');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Wound healing'){    
            var flag = all_activities.indexOf('Immunomodulatory');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Anti HIV' || all_activities[index] == 'Anti HSV'){    
            var flag = all_activities.indexOf('Antiviral');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Antibiofilm' || all_activities[index] == 'Anti Gram(+)' || all_activities[index] == 'Anti Gram(-)' || all_activities[index] == 'Anti TB' || all_activities[index] == 'Bacteriocins'){    
            var flag = all_activities.indexOf('Antibacterial/antibiotic');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Anti Yeast'){    
            var flag = all_activities.indexOf('Antifungal');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Antimalarial/antiplasmodial'){    
            var flag = all_activities.indexOf('Antiprotozoal');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Hemolytic'){    
            var flag = all_activities.indexOf('Cytolytic');
            delete all_activities[flag];
        }
        if (all_activities[index] == 'Antilisterial' || all_activities[index] == 'Anti MRSA'){    
            var flag = all_activities.indexOf('Anti Gram(+)');
            delete all_activities[flag];
        }
    }
    
    if (req.body['organisms[]'].includes('all') == true){
        if (req.body.uniprot == 'false'){
            if (all_activities != ''){
                const activities = await Activity.find({$and:[{"activity" : {"$in": all_activities}},{ "length": { $gte : parseInt(req.body['interval[]'][0])}},{ "length": { $lte : parseInt(req.body['interval[]'][1])}}]}).lean();
                res.send(activities);
            }
        }
        if (req.body.uniprot == 'true'){
            if (all_activities != ''){
                const activities = await Activity.find({$and:[{"activity" : {"$in": all_activities}}, {'uniprot_code': {$ne : ""}},{'uniprot_code': {$ne : "0"}}, { "length": { $gte : parseInt(req.body['interval[]'][0])}},{ "length": { $lte : parseInt(req.body['interval[]'][1])}}]}).lean();
                res.send(activities);
            }
        }
    }
    if (req.body['organisms[]'].includes("") == false && req.body['organisms[]'].includes('all') == false){
        if (req.body.uniprot == 'false'){
            if (all_activities != ''){
                const activities = await Activity.find({$and:[{"activity" : {"$in": all_activities}},{"organism_value" : {"$in": req.body['organisms[]']}},{ "length": { $gte : parseInt(req.body['interval[]'][0])}},{ "length": { $lte : parseInt(req.body['interval[]'][1])}}]}).lean();
                res.send(activities);
            }
        }
        if (req.body.uniprot == 'true'){
            if (all_activities != ''){
                const activities = await Activity.find({$and:[{"activity" : {"$in": all_activities}},{"organism_value" : {"$in": req.body['organisms[]']}}, {'uniprot_code': {$ne : ""}},{'uniprot_code': {$ne : "0"}}, { "length": { $gte : parseInt(req.body['interval[]'][0])}},{ "length": { $lte : parseInt(req.body['interval[]'][1])}}]}).lean();
                res.send(activities);
            }
        }
    }
}
indexCtrl.renderSequence = async(req,res) =>{
    const peptides = await Peptide.find({"id_sequence":req.query.id_sec}).lean();
    res.render('sequence', {peptides});
};
indexCtrl.renderDatabaseInformation = async(req,res) =>{
    res.render('database_information');
};
indexCtrl.renderCharacterization = async(req,res) =>{
    const statistics = await Statistic.find().lean();
    res.render('characterization', {statistics});
};
indexCtrl.getCharacterization = async(req,response) =>{    
    path_job = "./src/public/jobs/service1/"+req.body.time
    postData = JSON.stringify({
        'sequences': req.body.sequences,
        'time': req.body.time
    });
    const options = {
        host: 'localhost',
        port: 4000,
        method: 'POST',
        path: '/api/characterization/',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(postData)
        }
    };
    var req = http.request(options, (res) => {
        var data = ''
        res.on('data', (chunk) => {
            data = JSON.parse(chunk);
        });
        res.on('end', () => {
            console.log('No more data in response.');
            var str2 = JSON.parse(JSON.stringify(data));
            response.send(str2)
            setTimeout(function test(){
                rimraf(path_job, function () { console.log("done"); });
            },3600000);    // 1800000 = 30min
        });
    });
    
    req.on('error', (e) => {
        console.error(`problem with request: ${e.message}`);
    });
    req.write(postData);    
    req.end();
};
indexCtrl.renderClassification = async(req,res) =>{
    res.render('classification');
};
indexCtrl.getClassification = async(req,response) =>{
    response.setTimeout(3600000) // no timeout
    path = "./src/public/jobs/service2/"+req.body.time
    postData = JSON.stringify({
        'sequences': req.body.sequences,
        'time': req.body.time
    });
    const options = {
        host: 'localhost',
        port: 4000,
        method: 'POST',
        path: '/api/classification/',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(postData)
        }
    };
    var req = http.request(options, (res) => {
        var data = ''
        res.on('data', (chunk) => {
            data += chunk.toString();
        });
        res.on('end', () => {
            console.log('No more data in response.');
            var str2 = JSON.parse(data);
            response.send(str2)
        });
    });
    
    req.on('error', (e) => {
        console.error(`problem with request: ${e.message}`);
    });
    req.write(postData);    
    req.end();
};
indexCtrl.renderAlignment = async(req,res) =>{
    const organisms = await Organism.find({}).lean();
    res.render('alignment', {organisms});
};
indexCtrl.getAlignment = async(req,response) =>{
    path = "./src/public/jobs/service3/"+req.body.time
    postData = JSON.stringify({
        'sequences': req.body.sequences,
        'time': req.body.time
    });
    const options = {
        host: 'localhost',
        port: 4000,
        method: 'POST',
        path: '/api/alignment/',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(postData)
        }
    };
    var req = http.request(options, (res) => {
        var data = ''
        res.on('data', (chunk) => {
            data += chunk.toString();
        });
        res.on('end', () => {
            console.log('No more data in response.');
            var str2 = JSON.parse(data);
            response.send(str2)
        });
    });
    
    req.on('error', (e) => {
        console.error(`problem with request: ${e.message}`);
    });
    req.write(postData);    
    req.end();
};
indexCtrl.renderFrequency = async(req,res) =>{
    res.render('frequency');
};
indexCtrl.getFrequency = async(req,response) =>{
    path_job = "./src/public/jobs/service4/"+req.body.time
    postData = JSON.stringify({
        'sequences': req.body.sequences,
        'option': req.body.option,
        'time': req.body.time
    });    
    const options = {
        host: 'localhost',
        port: 4000,
        method: 'POST',
        path: '/api/frequency/',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(postData)
        }
    };
    var req = http.request(options, (res) => {
        var data = ''
        res.on('data', (chunk) => {
            data = JSON.parse(chunk);
        });
        res.on('end', () => {
            console.log('No more data in response.');
            var str2 = JSON.parse(JSON.stringify(data));
            response.send(str2)
            setTimeout(function test(){
                rimraf(path_job, function () { console.log("done"); });
            },3600000);    //10sec
        });
    });
    
    req.on('error', (e) => {
        console.log("ok")
        console.error(`problem with request: ${e.message}`);
    });
    req.write(postData);    
    req.end();
};
indexCtrl.renderEncoding = async(req,res) =>{
    res.render('encoding');
};
indexCtrl.getEncoding = async(req,response) =>{
    response.setTimeout(3600000) // no timeout
    path_job = "./src/public/jobs/service5/"+req.body.time+".tar.gz"
    postData = JSON.stringify({
        'sequences': req.body.sequences,
        'option': req.body.option,
        'time': req.body.time
    });    
    const options = {
        host: 'localhost',
        port: 4000,
        method: 'POST',
        path: '/api/encoding/',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(postData)
        }
    };
    var req = http.request(options, (res) => {
        var data = ''
        res.on('data', (chunk) => {
            data = JSON.parse(chunk);
        });
        res.on('end', () => {
            console.log('No more data in response.');
            var str2 = JSON.parse(JSON.stringify(data));
            response.send(str2);
            setTimeout(function test(){
                rimraf(path_job, function () { console.log("done"); });
            },3600000);    //10sec
        });
    });
    
    req.on('error', (e) => {
        console.error(`problem with request: ${e.message}`);
    });
    req.write(postData);    
    req.end();
};
indexCtrl.renderTraining = async(req,res) =>{
    res.render('training');
};
indexCtrl.getTraining = async(req,response) =>{
    response.setTimeout(3600000) // no timeout
    path_job = "./src/public/jobs/service6/"+req.body.time
    data = {
        "type_encoding" : req.body.encoding,
        "type_property" : req.body.properties,
        "type_response" : req.body.response,
        "algorithm": req.body.algorithm
    };
    await fs.writeFile("./src/public/jobs/service6/"+req.body.time+"/dict_response_input.json", JSON.stringify(data), function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The JSON file was written successfully");
});
    postData = JSON.stringify({
        'time': req.body.time,
    });    
    const options = {
        host: 'localhost',
        port: 4000,
        method: 'POST',
        path: '/api/training/',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(postData)
        }
    };
    var req = http.request(options, (res) => {
        var data = ''
        res.on('data', (chunk) => {
            data = JSON.parse(chunk);
        });
        res.on('end', () => {
            console.log('No more data in response.');
            if (data == "error"){
                response.send(JSON.stringify(data))
            }else{
                response.send(data)
            }
            setTimeout(function test(){
                rimraf(path_job, function () { console.log("done"); });
            },3600000);    //10sec
        });
    });
    req.on('error', (e) => {
        console.error(`problem with request: ${e.message}`);
    });
    req.write(postData);    
    req.end();
};

var storage1 = multer.diskStorage({ 
    
    destination: function (req, file, cb) { 
        var url_parts = url.parse(req.url, true);
        var query = url_parts.query;
        if (!fs.existsSync("./src/public/jobs/service6/"+query.time)){
            fs.mkdirSync("./src/public/jobs/service6/"+query.time);
        }
        cb(null, "./src/public/jobs/service6/"+query.time) 
    }, 
    filename: function (req, file, cb) {
        if (file.fieldname == "dataset"){
            cb(null, file.fieldname+".fasta") 
        } 
        else{
            cb(null, file.fieldname+".csv") 
        }
    } 
}) 

var upload1 = multer({  
    storage: storage1,  
}).any();

indexCtrl.uploadTraining = function (req, res, next) {     
    upload1(req,res,function(err) { 
        if(err) { 
            res.send(err) 
        } 
        else { 
            res.send({"upload":"ok"})
        } 
    }) 
};

indexCtrl.renderGlossary = async(req,res) =>{ 
    const statistics = await Statistic.find().lean();
    res.render('glossary', {statistics});
};
module.exports = indexCtrl;