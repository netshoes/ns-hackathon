package com.netshoes.matchnet.modulos.separator.gateway.impl;

import com.netshoes.matchnet.domain.sellerProducts.SellerProducts;
import com.netshoes.matchnet.modulos.separator.gateway.SmartSeparatorGateway;
import com.netshoes.matchnet.modulos.separator.gateway.feign.ProductSpliteratorFeignClient;
import com.netshoes.matchnet.modulos.separator.gateway.feign.json.SeparatorData;
import com.netshoes.matchnet.modulos.separator.gateway.feign.json.SeparatorRequestBody;
import com.netshoes.matchnet.modulos.separator.gateway.feign.json.SpliteratorResponseBody;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.List;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@Component
@RequiredArgsConstructor
public class SmartSeparatorGatewayImpl implements SmartSeparatorGateway {

    private final ProductSpliteratorFeignClient productSpliteratorFeignClient;

    @Override
    public SpliteratorResponseBody startSeparatorEngine(List<SellerProducts> sellerProducts) {
        SeparatorRequestBody requestBody = new SeparatorRequestBody();
        SeparatorData data = new SeparatorData();
        requestBody.setData(sellerProducts);
        return productSpliteratorFeignClient.startSeparatorEngine(requestBody);
    }
}