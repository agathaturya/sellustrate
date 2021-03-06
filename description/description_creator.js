//Jake Bildy, 2018

var request = require('request');

var KEYWORD = "computer mouse";
var QUALITY = 4;

var JSONSearchObject = {"search" : KEYWORD};
var responseJSON;
var descriptions;


request({
    url: "http://sellustrate.azurewebsites.net/desc",
    method: "POST",
    json: true,
    body: JSONSearchObject
}, function (error, response, body){
   // console.log(body);
    descriptions = body.toString().split(",");
    console.log(returnFinalDescription());
});




function qualityIntToDescription(QUALITY)
{
    switch(QUALITY) {
        case 0:
            return "The product is brand new and has never been opened.";
        case 1:
            return "The product is brand new, but already opened. Barely touched.";
        case 2:
            return "The product is brand new, but contains some defects. Still more than functional.";
        case 3:
            return "The product is in good condition, having been recently refurbished by the manufacturer.";
        case 4:
            return "The product is in good condition - recently refurbished.";
        case 5:
            return "The product is in absolute mint condition.";
        case 6:
            return "The product is in very good condition.";
        case 7:
            return "The product is used, but still in very good condition.";
        case 8:
            return "The product is quite well used, but still in an acceptable condition. Still works.";
        case 9:
            return "The product is very heavily used, and no longer functions.";

    }
}

function randomComment(NUMBER)
{
    switch(NUMBER){

        case 0:
            return " Definitely a great deal.";
        case 1:
            return " Hurry now before it's too late!";
        case 2:
            return " Going fast - make it yours today.";
        case 3:
            return " You don't find a lot of deals like this.";
        case 4:
            return " Definitely worth the price.";
        case 5:
            return " Deals like this are hard to come by.";
    }

}

function getCondition(){
    switch(QUALITY){
        case 0:
            return "New";
        case 1:
            return "New other";
        case 2:
            return "New with defects";
        case 3:
            return "Manufacturer refurbished";
        case 4:
            return "Seller refurbished";
        case 5:
            return "Used";
        case 6:
            return "Very Good";
        case 7:
            return "Good";
        case 8:
            return "Acceptable";
        case 9:
            return "For parts or not working";
    }
}

function returnFinalDescription()
{
    return "Selling " + KEYWORD + ": " + qualityIntToDescription(QUALITY) + randomComment(4);
}

function constructFinalJSON()
{
    return finalJSON = {
        "product": {
        "title": KEYWORD,
            "aspects": [
        ],
            "description": returnFinalDescription(),
            "imageUrls": [" "]
    },
        "condition": getCondition(),
        "packageWeightAndSize": {
        "packageType": "MAILING_BOX",
            "weight": {
            "value": 2,
                "unit": "POUND"
        }
    },
        "availability": {
        "shipToLocationAvailability": {
            "quantity": 1
        }
    }
    }
}

//Sends final JSON to server
request({
    url: "http://sellustrate.azurewebsites.net/final",
    method: "POST",
    json: true,
    body: constructFinalJSON()
}, function (error, response, body){

});
