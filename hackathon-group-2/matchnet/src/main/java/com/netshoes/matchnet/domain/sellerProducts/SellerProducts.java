package com.netshoes.matchnet.domain.sellerProducts;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

/**
 * Created by Grazeffe on 28/09/19.
 * https://github.com/Grazeffe
 */
@Data
@Document(collection = "sellerProducts")
@JsonIgnoreProperties(ignoreUnknown = true)
@NoArgsConstructor
public class SellerProducts {

    @Id
    private String id;
    private String nome;
    private Double precoDe;
    private Double precoPor;
    private Lojista lojista;
    private String imagem1;
    private String imagem2;
    private String imagem3;
    private String imagem4;
    private String valorGenero;
    private String departamento;
    private Double peso;
    private String marca;

    private LocalDateTime dataCriacao;
    private Dimensao dimensao;
    private String status;
    private String descricao;
    private String tamanho;
    private String tipoProduto;
    private String cor;
    private String idSkuOrigem;
    private Double quantidadeEstoque;
    private String skuNetshoes;
}