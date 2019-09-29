package com.netshoes.matchnet.gateway.mongo;

import com.netshoes.matchnet.domain.netsProducts.NetshoesProducts;
import com.netshoes.matchnet.domain.sellerProducts.SellerProducts;
import com.netshoes.matchnet.modulos.separator.gateway.feign.json.ClusteredProducts;

import java.util.List;

/**
 * Created by Grazeffe on 28/09/19.
 * https://github.com/Grazeffe
 */

public interface MongoGateway {

    void cadastrarTodosSeller(List<SellerProducts> sellerProducts);
    void cadastrarTodosNets(List<NetshoesProducts> netsProducts);
    List<SellerProducts> buscarTodosSellerProducts();
    void saveCluesteredProducts(List<ClusteredProducts> clusteredProducts);
}