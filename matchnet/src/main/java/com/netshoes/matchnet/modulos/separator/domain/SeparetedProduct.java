package com.netshoes.matchnet.modulos.separator.domain;

import com.netshoes.matchnet.domain.sellerProducts.Dimensao;
import com.netshoes.matchnet.domain.sellerProducts.Lojista;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

/**
 * Created by Grazeffe on 28/09/19.
 * https://github.com/Grazeffe
 */
@Data
@Document
public class SeparetedProduct {

    @Id
    private String id;
    private String nome;
    private Lojista lojista;
    private Double precoDe;
    private Double precoPor;
    private String imagem1;
    private String valorGenero;
    private String departamento;
    private Double peso;
    private String marca;
    private Dimensao dimensao;
    private String descricao;
    private String tamanho;
    private String tipoProduto;
    private String cor;
    private String idSkuOrigem;
    private Double quantidadeEstoque;
    private String skuNetshoes;
    private Cluster cluster;
}