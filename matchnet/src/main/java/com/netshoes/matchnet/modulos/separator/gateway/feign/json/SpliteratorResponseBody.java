package com.netshoes.matchnet.modulos.separator.gateway.feign.json;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class SpliteratorResponseBody {
    private List<ClusteredProducts> response;
}