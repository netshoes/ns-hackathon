package com.netshoes.matchnet.modulos.separator.usecase;

import com.netshoes.matchnet.domain.sellerProducts.SellerProducts;
import com.netshoes.matchnet.gateway.mongo.MongoGateway;
import com.netshoes.matchnet.modulos.separator.gateway.SmartSeparatorGateway;
import com.netshoes.matchnet.modulos.separator.gateway.feign.json.ClusteredProducts;
import com.netshoes.matchnet.modulos.separator.separatorConverter.SeparatorConverterUC;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.List;

/**
 * Created by Grazeffe on 28/09/19.
 * https://github.com/Grazeffe
 */
@Component
@RequiredArgsConstructor
public class SmartSeparator {

    private final MongoGateway mongoGateway;
    private final SmartSeparatorGateway smartSeparatorGateway;
    private final SeparatorConverterUC separatorConverterUC;

    public List<ClusteredProducts> execute() {
        List<SellerProducts> sellerProducts = mongoGateway.buscarTodosSellerProducts();
        return separatorConverterUC.spliteratorResponseToClusteredProducts(smartSeparatorGateway.startSeparatorEngine(sellerProducts));
    }
}