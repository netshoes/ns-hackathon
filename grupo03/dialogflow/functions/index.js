/**
 * Copyright 2017 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

'use strict';
const axios = require('axios');
const functions = require('firebase-functions');
const { WebhookClient } = require('dialogflow-fulfillment');
const { Card, Suggestion } = require('dialogflow-fulfillment');
const { Carousel } = require('actions-on-google');
// const dialogflow = require('dialogflow');

process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements

// URLs for images used in card rich responses
const imageUrl = 'https://developers.google.com/actions/images/badges/XPM_BADGING_GoogleAssistant_VER.png';
const imageUrl2 = 'https://lh3.googleusercontent.com/Nu3a6F80WfixUqf_ec_vgXy_c0-0r4VLJRXjVFF_X_CIilEu8B9fT35qyTEj_PEsKw';
const linkUrl = 'https://assistant.google.com/';

// const sessionClient = new dialogflow.SessionsClient();

axios.defaults.headers.common['Authorization'] = "Bearer ya29.c.Kl6RB0CW-5acKRVA54nXVpN92TIjnx5Fqzkzzn7PrqHMtyiQYuhyuf1kpqt0mGxT-Pfahw2C8VXUEog_RjAk1_Iraajuia4dENLEkwMugOeO_Z4H1y08gj5XOnLBoLyB";
exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  const agent = new WebhookClient({ request, response });
  console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
  console.log('Dialogflow Request body: ' + JSON.stringify(request.body));

  function googleAssistantOther(agent) {
    let conv = agent.conv(); // Get Actions on Google library conversation object
    conv.ask('Please choose an item:'); // Use Actions on Google library to add responses
    conv.ask(new Carousel({
      title: 'Google Assistant',
      items: {
        'WorksWithGoogleAssistantItemKey': {
          title: 'Works With the Google Assistant',
          description: 'If you see this logo, you know it will work with the Google Assistant.',
          image: {
            url: imageUrl,
            accessibilityText: 'Works With the Google Assistant logo',
          },
        },
        'GoogleHomeItemKey': {
          title: 'Google Home',
          description: 'Google Home is a powerful speaker and voice Assistant.',
          image: {
            url: imageUrl2,
            accessibilityText: 'Google Home'
          },
        },
      },
    }));
    // Add Actions on Google library responses to your agent's response
    agent.add(conv);
  }

  function welcome(agent) {

    axios.get('https://www.google.com')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })

    agent.add(`Welcome to my agent!`);
  }

  function fallback(agent) {

    console.log("dshfkjldshfklhdslkfhdl");
    axios.get('https://us-central1-hackathon-2019-254113.cloudfunctions.net/purchase_status')
      .then(function (response) {

        console.log(response.data.status);

        agent.add(response.data.status);
        // agent.add(`I'm sorry, can you try again?`);

      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })

      postaLa()

  }

  function postaLa(){
    // const sessionPath = sessionClient.sessionPath("hackathon-03", 123456789);
    axios.post('https://dialogflow.googleapis.com/v2/projects/hackathon-03/agent/sessions/1122334455:detectIntent',
    {
      query_input:{
        text:{
          text:'do something pls',
          language_code:'pt-BR'
        }
      }
    }).then(function (response) {
      console.log("retornooouuuuuu");
      console.log(response);
    }).catch(function (error) {
      console.log("ai meu rim " + error);
      console.log(error);
    });
  }

  function other(agent) {
    agent.add(`This message is from Dialogflow's Cloud Functions for Firebase editor!`);
    agent.add(new Card({
        title: `Title: this is a card title`,
        imageUrl: imageUrl,
        text: `This is the body text of a card.  You can even use line\n  breaks and emoji! 💁`,
        buttonText: 'This is a button',
        buttonUrl: linkUrl
      })
    );
    agent.add(new Suggestion(`Quick Reply`));
    agent.add(new Suggestion(`Suggestion`));
    agent.setContext({ name: 'weather', lifespan: 2, parameters: { city: 'Rome' }});
  }

  // Run the proper handler based on the matched Dialogflow intent
  let intentMap = new Map();
  intentMap.set('saudacao', welcome);
  intentMap.set('Default Fallback Intent', fallback);
  // if requests for intents other than the default welcome and default fallback
  // is from the Google Assistant use the `googleAssistantOther` function
  // otherwise use the `other` function
  if (agent.requestSource === agent.ACTIONS_ON_GOOGLE) {
    intentMap.set(null, googleAssistantOther);
  } else {
    intentMap.set(null, other);
  }
  agent.handleRequest(intentMap);
});
