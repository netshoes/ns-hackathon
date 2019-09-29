package com.netshoes.matchnet.gateway.http.json;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@Data
@JsonIgnoreProperties(ignoreUnknown = true)
public class SkuNets {
    private Sku sku;
}