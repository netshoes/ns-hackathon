package com.netshoes.matchnet.modulos.separator.gateway.feign;

import com.netshoes.matchnet.modulos.separator.gateway.feign.json.SeparatorRequestBody;
import com.netshoes.matchnet.modulos.separator.gateway.feign.json.SpliteratorResponseBody;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@FeignClient(name = "ProductSpliteratorFeignClient",
        url = "http://10.0.65.49:5001")
public interface ProductSpliteratorFeignClient {

    @PostMapping(value = "/sellerProducts",
            produces = MediaType.APPLICATION_JSON_VALUE)
    SpliteratorResponseBody startSeparatorEngine(@RequestBody final SeparatorRequestBody requestBody);
}