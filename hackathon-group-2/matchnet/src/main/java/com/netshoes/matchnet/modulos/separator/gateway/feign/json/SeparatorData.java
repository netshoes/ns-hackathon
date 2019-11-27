package com.netshoes.matchnet.modulos.separator.gateway.feign.json;

import com.netshoes.matchnet.domain.sellerProducts.SellerProducts;
import lombok.Data;

import java.util.List;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@Data
public class SeparatorData {

    private List<SellerProducts> sellerProducts;
}