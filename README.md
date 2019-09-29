<p align="center">
  <img src="https://user-images.githubusercontent.com/28030519/64352699-ded39200-cfd2-11e9-91a4-ed054d89ed97.jpg" width="60%" title="Hackathon Netshoes">
</p>

# Hackathon Netshoes

A Netshoes foi fundada em janeiro de 2000 como uma loja física de calçados em um estacionamento em São Paulo. Em 2002 iniciamos nossas operações online e em 2007, fechamos nossas lojas físicas e migramos para um negócio 100% online.

Hoje, nossa stack conta com tecnologias de ponta, como banco de dados não-relacionais, softwares de mensageria, java reativo e arquitetura em microserviços. Seguimos inovando e nos desafiando. 

Esse repositório será nosso principal meio de compartilhamento da informação. Nele, você encontrará o regulamento da nossa maratona. Alguns dias antes disponibilizaremos aqui os temas do Hackathon Netshoes. Venha viver essa experiência!

# Regras do jogo

- 5 pessoas por time.
- Ao final do evento os grupos deverão ter submetido uma Pull Request no repositório Git da Hackathon - https://github.com/netshoes/ns-hackathon.
- Ao final do evento os grupos apresentarão as soluções desenvolvidas para a banca de jurados.
- A apresentação será em formato de pitch, com duração de no máximo 3 minutos. Os jurados terão 2 minutos para realizar perguntas.

## Metodologia de avaliação
Os projetos propostos serão avaliados pelos jurados e receberão notas ao final. O cálculo será feito conforme o seguinte racional:

```NOTA FINAL = Σ [ (Nota critério 1) + (Nota critério 2) + (Nota critério 3)+ (Nota critério 4) ]```

Os critérios de avaliação utilizados pelos jurados para definir quais das soluções propostas pelos grupos serão vencedoras da Hackathon são:
- *Estrutura da solução:* Diz respeito ao racional proposto pelo time para solucionar o desafio.
- *Relevância com o tema:* Diz respeito a quanto a solução proposta resolve o desafio.
- *Completude:* Diz respeito a quanto a solução proposta está funcional.
- *Pitch:* Diz respeito a qualidade e clareza da apresentação.

Cada critério será avaliado conforme a escala abaixo:
- *Não atende:* 0 ponto.
- *Atende parcialmente:* 1 ponto.
- *Atende:* 2 pontos.
- *Supera:* 3 pontos. 

Ao final, serão somadas as notas de todos os jurados para determinar a pontuação final do grupo.
Em caso de empate, os jurados decidirão entre eles quais serão os grupos vencedores.

# Desafios
## Autoatendimento
Como melhorar a experiência de autoatendimento do cliente na Netshoes de forma inovadora, adaptativa e evolutiva.

#### Motivação
Com o rápido crescimento do e-commerce no Brasil e a mudança no conceito de experiência de compra, torna-se também necessária a adaptação das formas de atendimento ao usuário antes, durante e depois do processo de compra. Em um mundo de tecnologias self service, o autoatendimento emerge como aliado na experiência do usuário para proporcionar um atendimento mais rápido, barato e efetivo.

### Trabalhado a ser realizado
Quando o cliente precisar obter suporte sobre qualquer tema relacionado à Netshoes, quero oferecer a ele um atendimento automatizado inteligente, que seja efetivo na resolução das suas questões, sem a necessidade de iteração humana por parte da Netshoes.

#### KPIs de sucesso
-	Aumento da quantidade de mensagens whatsapp válidas.
-	Diminuição dos contatos no SAC Netshoes.
-	Aumento da base ativa.

## Curadoria de produtos marketplace

Como automatizar o processo de avaliação e seleção de produtos no modelo de marketplace de forma ágil permitindo match de produtos garantindo a qualidade do catálogo de produtos da Netshoes.

#### Motivação
Um dos grandes desafios em escalar a venda de produtos utilizando o modelo de marketplace, em que uma loja centraliza a venda de diversos lojistas, há frequentemente a necessidade de avaliação e seleção manual dos produtos a serem disponibilizados para venda, de forma a garantir não só a idoneidade e confiabilidade do lojista, mas também a unificação de produtos iguais de diferentes lojistas e eliminação de produtos incompatíveis com o negócio ou imagem e conteúdo nocivos.
Este processo de curadoria tende a ser demorado e sujeito a erros humanos, fazendo com que leve tempo para que novos produtos sejam disponibilizados para venda e que a qualidade do catálogo de produtos seja comprometida.

### Trabalho a ser realizado
Quando um lojista disponibilizar um produto para venda na plataforma de marketplace da Netshoes, quero que esse item esteja disponível para venda em pouco tempo, sem ferir a qualidade do catálogo do site, para garantir o incremento da base de produtos de lojistas e, consequentemente, da venda desses itens.
Por qualidade de catálogo deve-se considerar os fatores abaixo:
-	Ausência de produtos repetidos na busca de itens.
-	Produtos com imagens de alta resolução.
-	Descrição dos produtos com riqueza de detalhes e informação.
-	Descrição sem erros de português, ortográficos, etc.
-	Remoção de produtos incompatíveis com o negócio.

#### KPIs de sucesso
-	Diminuição do tempo de triagem manual dos produtos.
-	Diminuição do tempo para aprovação de um produto de lojista.
-	Aumento na quantidade de produtos ativados ao dia.

# Primeiros passos
1.	Conectar na Wifi do evento:
  -	SSID: H4CK47H0N – Netshoes
  -	Password: 4sfvG$%qH+
2. Acessar [Google Cloud Console](https://console.cloud.google.com) com as credenciais do grupo.
  - *NOTA:* As credenciais de acesso serão disponibilizados aos grupos no dia do evento.
3. Selecionar o projeto ```hackathon-xx```, sendo ```xx``` o número do seu grupo.
4. Na aba recursos, acessar o ```Big Query```.
  - Aqui você encontrará as bases de dados necessárias para a realização dos desafios - ```dadosBrutos```. 
  - Seu grupo terá permissão de escrita/leitura nesse dataset. **CUIDADO: havendo necessidade de escrita, recomendamos copiar a tabela e não alterar a original.**
  
# Extras
#### Integração com whats

<p align="center">
  <img src="https://user-images.githubusercontent.com/28030519/65807581-73aa5500-e165-11e9-860c-e080a1ac63c5.png" width="60%" title="Hackathon Netshoes">
</p>

#### Mock de Apis de Pedido

Status do pedido: https://us-central1-hackathon-2019-254113.cloudfunctions.net/purchase_status

Status da troca: https://us-central1-hackathon-2019-254113.cloudfunctions.net/exchange_status

Saldo do voucher: https://us-central1-hackathon-2019-254113.cloudfunctions.net/voucher_balance

#### Para publicar suas mensagens para o whats netshoes:
Chamda Post para: https://us-central1-hackathon-2019-254113.cloudfunctions.net/message 

```
{
  "message": "str",
  "phone": "11999999999"
}
```

#### Para consumir as mensagens que vem do whats netshoes:
Configure a subscription correspondente ao grupo:

`hackathon01`
`hackathon02`
`hackathon03`
`hackathon04`
`hackathon05`
`hackathon06`
`hackathon07`
`hackathon08`
`hackathon09`
`hackathon10`
`hackathon11`



