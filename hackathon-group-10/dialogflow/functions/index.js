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
const cheerio = require('cheerio')

process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements

exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  const agent = new WebhookClient({ request, response });
  console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
  console.log('Dialogflow Request body: ' + JSON.stringify(request.body));

  async function pedidoIntent(agent) {
    const pedidos = [{
        nome: 'Puma1',
        numero_pedido: 10210209
    },{
        nome: 'Puma2',
        numero_pedido: 10210209
    },
    {
        nome: 'Puma3',
        numero_pedido: 10210209
    }];

    for(let i = 0; i < 3; i++) {
        let resultado = await axios.get('https://us-central1-hackathon-2019-254113.cloudfunctions.net/purchase_status')
        pedidos[i].status = resultado.data.status;
    }

    const fim = [];

    const apresentacao = 'Encontramos os seguintes pedidos e seus respectivos status no nosso sistema.\n';
    fim.push(apresentacao);

    pedidos.forEach(pedido => {
        const {nome, numero_pedido, status} = pedido;
        fim.push('Nome: '+nome+'\nNumero: '+numero_pedido+'\nStatus: '+status);
    });

    agent.add(fim.join('\n\n'));
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


  async function fallback(agent) {

    console.log("dshfkjldshfklhdslkfhdl");
    var test = await axios.get('https://us-central1-hackathon-2019-254113.cloudfunctions.net/purchase_status')
      // .then(function (response) {
      
      //   console.log(response.data.status);
      //   response.fulfillmentText = "sdkf;lskdfh;lsdhf;d";
        // agent.add("dhfsdklfhlskdhfkldslkhflkdflksdkhfksdhflksdhklfhlksdhfklhdlkf");
        // agent.add(`I'm sorry, can you try again?`);

      // })
      // .catch(function (error) {
      //   console.log(error);
      // })

      agent.add(test.data.status);

  }

  async function queroComprar(agent) {
    const {produto, color} = agent.parameters
    if(produto.length == 0) agent.add('Não encontrei nenhum produto com essa descrição');
    let param = produto.join('+');
    if(color !== '') param += '+' + color;
    param = 'https://www.netshoes.com.br/busca?nsCat=Natural&q=' + param;

    const res = await axios.get(param)
    const $ = cheerio.load(res.data)
    const nome_produto = $('a.item-card__description__product-name', res.data).first().text();

    if(nome_produto.length == 0) {
        agent.add('Não encontrei nenhum produto com a descrição fornecida ): prometo me esforçar mais na próxima vez!');
        return;
    }
    const link_produto = $('a.item-card__description__product-name', res.data).first().attr('href')

    agent.add('Encontrei ' + nome_produto + ' para você! (:\nLink para comprar: '+link_produto+'\n\nPara mais produtos na categoria: '+param) 
  }

  async function voucherStatus(agent) {
      var test = await axios.get('https://us-central1-hackathon-2019-254113.cloudfunctions.net/voucher_balance')
      if(test.data.value === 0) {
        let messagem = 'Seu saldo de "Vouchers" está vazio. Se houver alguma análise pendente, será mostrada abaixo:\n\nStatus da troca: ';
        const status_troca = await axios.get('https://us-central1-hackathon-2019-254113.cloudfunctions.net/exchange_status');
        agent.add(messagem + status_troca.data.status);
      } else agent.add('Saldo: R$' + (test.data.value / 100).toFixed(2));
  }

  // Run the proper handler based on the matched Dialogflow intent
  let intentMap = new Map();
  intentMap.set('Saudacao', welcome);
  intentMap.set('Pedido', pedidoIntent);
  intentMap.set('Default Fallback Intent', fallback);
  intentMap.set('Voucher', voucherStatus);
  intentMap.set('queroComprar', queroComprar);
  // if requests for intents other than the default welcome and default fallback
  // is from the Google Assistant use the `googleAssistantOther` function
  // otherwise use the `other` function
  agent.handleRequest(intentMap);
});
