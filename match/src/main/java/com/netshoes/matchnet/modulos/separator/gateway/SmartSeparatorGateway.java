package com.netshoes.matchnet.modulos.separator.gateway;

import com.netshoes.matchnet.domain.sellerProducts.SellerProducts;
import com.netshoes.matchnet.modulos.separator.gateway.feign.json.SpliteratorResponseBody;

import java.util.List;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */

public interface SmartSeparatorGateway {

    SpliteratorResponseBody startSeparatorEngine(List<SellerProducts> sellerProducts);
}