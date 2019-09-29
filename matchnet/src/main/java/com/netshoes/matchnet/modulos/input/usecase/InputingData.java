package com.netshoes.matchnet.modulos.input.usecase;

import com.netshoes.matchnet.domain.netsProducts.NetshoesProducts;
import com.netshoes.matchnet.domain.sellerProducts.SellerProducts;
import com.netshoes.matchnet.gateway.http.json.SkuNets;
import com.netshoes.matchnet.gateway.mongo.MongoGateway;
import com.netshoes.matchnet.modulos.input.productConverter.ProductConverterUC;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Grazeffe on 28/09/19.
 * https://github.com/Grazeffe
 */

@Component
@RequiredArgsConstructor
public class InputingData {

    private final MongoGateway mongoGateway;
    private final ProductConverterUC productConverterUC;

    public void inputSellerProducts(List<SellerProducts> sellerProducts) {
        mongoGateway.cadastrarTodosSeller(sellerProducts);
    }

    public void inputNetsProducts(List<SkuNets> netsProducts) {
        List<NetshoesProducts> netshoesProductsList = new ArrayList<>();
        try {
            netsProducts.forEach(netsProduct -> netshoesProductsList.add(productConverterUC.skuToNetsProduct(netsProduct)));
            mongoGateway.cadastrarTodosNets(netshoesProductsList);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}