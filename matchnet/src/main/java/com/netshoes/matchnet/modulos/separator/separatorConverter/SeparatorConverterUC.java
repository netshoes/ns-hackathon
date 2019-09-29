package com.netshoes.matchnet.modulos.separator.separatorConverter;

import com.netshoes.matchnet.modulos.separator.gateway.feign.json.ClusteredProducts;
import com.netshoes.matchnet.modulos.separator.gateway.feign.json.SpliteratorResponseBody;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@Component
@RequiredArgsConstructor
public class SeparatorConverterUC {

    public List<ClusteredProducts> spliteratorResponseToClusteredProducts(final SpliteratorResponseBody responseBody) {
        List<ClusteredProducts> clusteredProductList = new ArrayList<>();
        clusteredProductList.addAll(responseBody.getResponse());
        return clusteredProductList;
    }
}