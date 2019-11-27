package com.netshoes.matchnet.modulos.separator.gateway.feign.json;

import lombok.Data;
import org.springframework.data.annotation.Id;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@Data
public class Products {

    @Id
    private String id;
    private String distance;
}