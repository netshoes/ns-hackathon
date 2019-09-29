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


#### Credentials for Pub/Sub
```
{
  "type": "service_account",
  "project_id": "hackathon-2019-254113",
  "private_key_id": "4b5cb33d07cb613bda5cb9c146e0c7beae16b81b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDAcgpMIfOtn9Y9\nodkvJ53CfrjWJv4GnoeO6Gwuiu/FjSc6mozYEAtYn1EX6T+Qww8qv0+WtP0fDSeB\nh2jI6tfp/m/XOjMse3GvwqHpG60fEBTqcgkE9iX63WMNaieRC6RbM94zuDoXbvuo\nR6LzJt01FuGqm4YkCsml87sCmsxxW41wEfk78xk4ahKjV1HvbU/9KTuYq5psqr1V\n/Jvh/FunjqxIF1bZl0ZCevP9ob/6X3r9g8VyZKI0JS6P1TgVuEmztF2rm8OMcHwF\nxr7WOa0Y5r7WPBcFAOJz6oHKw8Axy+clR9pP0KRmxGuqHExlRUF2DcmUp/R+agmo\n7nT2wuJ7AgMBAAECggEAAds6fAJPHDhnI4nNzzbnM4SjZSXex7ZPfjXpbX5msHME\nWIxyqNQL++MRMsu7Zx+ERPK6vbczKhW9Mmz00tDddcsXIkQCd5MSPnh61gLITXIp\nPDaGsJ6CVwEK9OSABy/DBTRe6b24oqthr4A0NgM96EaGPXOBA0WsLROEsEjW2zGG\n3sIhKKCNuq1ZgS2+ISqbzvBzwQggooSdARTaKpHKOgzzwW3wVhTEIPLYnMAgBOVJ\n998BC5TatSrrFLEMjTSGO8xrzks3RnIBOjPRod9D6cFfFPGdOx1wad2hQL/NzVaG\nJK7UnUEDW3w7ad5l0w44E0XgAwoSlaMi/adHYjH22QKBgQDpATbf1LQ0UEvaSQKD\nznifaM6LbF4I4rDl/xqd1y4KflIWmpWUykwOLq0zsfvwRv/aqHtvJxnZTpu8oTuQ\nWMbsa5FQzeCSYERhTksGL+9F9M+oTdHhNMi6ICiPyyJ4NMJ+8QY7XnBpyyA65/Ih\nmAj8jXEU6LfDMOZlke3FKde6qQKBgQDTcBwO1vN2z0ogW+lGR6Ke3gtAzUL2u/Ar\nX46LzRuh6vqa5BQtQmRdoh5S7d7xIFSWo5qDjr1Dcu3IyIENmZqnI92uHb4s5xav\nKZChTPjmzZVUXLeuvVDvFah695TOXoOl/+8W47CMdsj7iTVKJeWhdI3ztcg85YwJ\neNWyE7QugwKBgQCvI2+IzUvqqpRpbkmKo269e70MxZblHOgU6SyrieucjZjMTsOy\nhGCopGMiIV2bHPMB+3RUd1KRqemb3qFz/ZcAbFZdI3Ly85NShNQVwYAb2EkiW+Qv\nYEqkxLlYZDrzmcy8OBUUGQdsLfd6749ruui+VN6z9bzy5dW4cPkFI095iQKBgQCG\nFEbGpkp3ohW4lXBFT/Hw2o+6RS/ctOslJhCH2MZYFGFczZt54+svcTnXjt5cfAsI\nB7FZEbA1UHE3bOZhkHGA4f6Whmfto5E//JSppN0Fx4KVn8IfPhBPvKU9bTjg8RB8\nuOKN2k8/k6f50lWHsqZ+jyHhVPoom8wEyaqBpXsSLwKBgQDFAaqozLAyAgqMAo/H\nYMneaRXtSd0f0DR97o0HGYWYqTQHAtZQHuhi5ni22ZI3n4qaCM9Z+1woS53wvj+b\nUSG4yz9eOYsywsZRhnVknoClVMa2hQcJX0fy0J5xCn68GRDsToH/Hh+5yvEf4xED\nvZDCU9i1bWcmzUkSsHP2d22zjg==\n-----END PRIVATE KEY-----\n",
  "client_email": "ff-whastsapp@hackathon-2019-254113.iam.gserviceaccount.com",
  "client_id": "115589535227665625718",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ff-whastsapp%40hackathon-2019-254113.iam.gserviceaccount.com"
}
```
#### Credentials for Pub/Sub base64 encoded

```
ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAiaGFja2F0aG9uLTIwMTktMjU0MTEzIiwKICAicHJpdmF0ZV9rZXlfaWQiOiAiNGI1Y2IzM2QwN2NiNjEzYmRhNWNiOWMxNDZlMGM3YmVhZTE2YjgxYiIsCiAgInByaXZhdGVfa2V5IjogIi0tLS0tQkVHSU4gUFJJVkFURSBLRVktLS0tLVxuTUlJRXZ3SUJBREFOQmdrcWhraUc5dzBCQVFFRkFBU0NCS2t3Z2dTbEFnRUFBb0lCQVFEQWNncE1JZk90bjlZOVxub2Rrdko1M0NmcmpXSnY0R25vZU82R3d1aXUvRmpTYzZtb3pZRUF0WW4xRVg2VCtRd3c4cXYwK1d0UDBmRFNlQlxuaDJqSTZ0ZnAvbS9YT2pNc2UzR3Z3cUhwRzYwZkVCVHFjZ2tFOWlYNjNXTU5haWVSQzZSYk05NHp1RG9YYnZ1b1xuUjZMekp0MDFGdUdxbTRZa0NzbWw4N3NDbXN4eFc0MXdFZms3OHhrNGFoS2pWMUh2YlUvOUtUdVlxNXBzcXIxVlxuL0p2aC9GdW5qcXhJRjFiWmwwWkNldlA5b2IvNlgzcjlnOFZ5WktJMEpTNlAxVGdWdUVtenRGMnJtOE9NY0h3RlxueHI3V09hMFk1cjdXUEJjRkFPSno2b0hLdzhBeHkrY2xSOXBQMEtSbXhHdXFIRXhsUlVGMkRjbVVwL1IrYWdtb1xuN25UMnd1SjdBZ01CQUFFQ2dnRUFBZHM2ZkFKUEhEaG5JNG5Oenpibk00U2paU1hleDdaUGZqWHBiWDVtc0hNRVxuV0l4eXFOUUwrK01STXN1N1p4K0VSUEs2dmJjektoVzlNbXowMHREZGRjc1hJa1FDZDVNU1BuaDYxZ0xJVFhJcFxuUERhR3NKNkNWd0VLOU9TQUJ5L0RCVFJlNmIyNG9xdGhyNEEwTmdNOTZFYUdQWE9CQTBXc0xST0VzRWpXMnpHR1xuM3NJaEtLQ051cTFaZ1MyK0lTcWJ6dkJ6d1FnZ29vU2RBUlRhS3BIS09nenp3VzN3VmhURUlQTFluTUFnQk9WSlxuOTk4QkM1VGF0U3JyRkxFTWpUU0dPOHhyemtzM1JuSUJPalBSb2Q5RDZjRmZGUEdkT3gxd2FkMmhRTC9OelZhR1xuSks3VW5VRURXM3c3YWQ1bDB3NDRFMFhnQXdvU2xhTWkvYWRIWWpIMjJRS0JnUURwQVRiZjFMUTBVRXZhU1FLRFxuem5pZmFNNkxiRjRJNHJEbC94cWQxeTRLZmxJV21wV1V5a3dPTHEwenNmdndSdi9hcUh0dkp4blpUcHU4b1R1UVxuV01ic2E1RlF6ZUNTWUVSaFRrc0dMKzlGOU0rb1RkSGhOTWk2SUNpUHl5SjROTUorOFFZN1huQnB5eUE2NS9JaFxubUFqOGpYRVU2TGZETU9abGtlM0ZLZGU2cVFLQmdRRFRjQndPMXZOMnowb2dXK2xHUjZLZTNndEF6VUwydS9BclxuWDQ2THpSdWg2dnFhNUJRdFFtUmRvaDVTN2Q3eElGU1dvNXFEanIxRGN1M0l5SUVObVpxbkk5MnVIYjRzNXhhdlxuS1pDaFRQam16WlZVWExldXZWRHZGYWg2OTVUT1hvT2wvKzhXNDdDTWRzajdpVFZLSmVXaGRJM3p0Y2c4NVl3SlxuZU5XeUU3UXVnd0tCZ1FDdkkyK0l6VXZxcXBScGJrbUtvMjY5ZTcwTXhaYmxIT2dVNlN5cmlldWNqWmpNVHNPeVxuaEdDb3BHTWlJVjJiSFBNQiszUlVkMUtScWVtYjNxRnovWmNBYkZaZEkzTHk4NU5TaE5RVndZQWIyRWtpVytRdlxuWUVxa3hMbFlaRHJ6bWN5OE9CVVVHUWRzTGZkNjc0OXJ1dWkrVk42ejlienk1ZFc0Y1BrRkkwOTVpUUtCZ1FDR1xuRkViR3BrcDNvaFc0bFhCRlQvSHcybys2UlMvY3RPc2xKaENIMk1aWUZHRmN6WnQ1NCtzdmNUblhqdDVjZkFzSVxuQjdGWkViQTFVSEUzYk9aaGtIR0E0ZjZXaG1mdG81RS8vSlNwcE4wRng0S1ZuOElmUGhCUHZLVTliVGpnOFJCOFxudU9LTjJrOC9rNmY1MGxXSHNxWitqeUhoVlBvb204d0V5YXFCcFhzU0x3S0JnUURGQWFxb3pMQXlBZ3FNQW8vSFxuWU1uZWFSWHRTZDBmMERSOTdvMEhHWVdZcVRRSEF0WlFIdWhpNW5pMjJaSTNuNHFhQ005Wisxd29TNTN3dmorYlxuVVNHNHl6OWVPWXN5d3NaUmhuVmtub0NsVk1hMmhRY0pYMGZ5MEo1eENuNjhHUkRzVG9IL0hoKzV5dkVmNHhFRFxudlpEQ1U5aTFiV2NtelVrU3NIUDJkMjJ6amc9PVxuLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLVxuIiwKICAiY2xpZW50X2VtYWlsIjogImZmLXdoYXN0c2FwcEBoYWNrYXRob24tMjAxOS0yNTQxMTMuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLAogICJjbGllbnRfaWQiOiAiMTE1NTg5NTM1MjI3NjY1NjI1NzE4IiwKICAiYXV0aF91cmkiOiAiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tL28vb2F1dGgyL2F1dGgiLAogICJ0b2tlbl91cmkiOiAiaHR0cHM6Ly9vYXV0aDIuZ29vZ2xlYXBpcy5jb20vdG9rZW4iLAogICJhdXRoX3Byb3ZpZGVyX3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vb2F1dGgyL3YxL2NlcnRzIiwKICAiY2xpZW50X3g1MDlfY2VydF91cmwiOiAiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vcm9ib3QvdjEvbWV0YWRhdGEveDUwOS9mZi13aGFzdHNhcHAlNDBoYWNrYXRob24tMjAxOS0yNTQxMTMuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iCn0K
```

