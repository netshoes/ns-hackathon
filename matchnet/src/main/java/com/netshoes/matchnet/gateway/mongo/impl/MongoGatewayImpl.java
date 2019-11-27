package com.netshoes.matchnet.gateway.mongo.impl;

import com.netshoes.matchnet.domain.netsProducts.NetshoesProducts;
import com.netshoes.matchnet.domain.sellerProducts.SellerProducts;
import com.netshoes.matchnet.gateway.mongo.MongoGateway;
import com.netshoes.matchnet.gateway.mongo.repository.ClusteredProductsRepository;
import com.netshoes.matchnet.gateway.mongo.repository.NetsProductsRepository;
import com.netshoes.matchnet.gateway.mongo.repository.SellerProductsRepository;
import com.netshoes.matchnet.modulos.separator.gateway.feign.json.ClusteredProducts;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.List;

/**
 * Created by Grazeffe on 28/09/19.
 * https://github.com/Grazeffe
 */
@Component
@RequiredArgsConstructor
public class MongoGatewayImpl implements MongoGateway {

    private final SellerProductsRepository sellerProductsRepository;
    private final ClusteredProductsRepository clusteredProductsRepository;
    private final NetsProductsRepository netsProductsRepository;

    public void cadastrarTodosSeller(List<SellerProducts> sellerProducts) {
        sellerProductsRepository.saveAll(sellerProducts);
    }

    @Override
    public void cadastrarTodosNets(List<NetshoesProducts> netsProducts) {
        netsProductsRepository.saveAll(netsProducts);
    }

    @Override
    public List<SellerProducts> buscarTodosSellerProducts() {
        return sellerProductsRepository.findAll();
    }

    @Override
    public void saveCluesteredProducts(List<ClusteredProducts> clusteredProducts) {
        clusteredProductsRepository.saveAll(clusteredProducts);
    }
}