package com.netshoes.matchnet.modulos.input.productConverter;

import com.netshoes.matchnet.domain.netsProducts.NetshoesProducts;
import com.netshoes.matchnet.gateway.http.json.Configurations;
import com.netshoes.matchnet.gateway.http.json.Sku;
import com.netshoes.matchnet.gateway.http.json.SkuNets;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@Component
@RequiredArgsConstructor
public class ProductConverterUC {

    public NetshoesProducts skuToNetsProduct(SkuNets skuN) {
        Sku sku = skuN.getSku();
        return NetshoesProducts.builder()
                .id(sku.getId().getCode())
                .dimension(sku.getDimension())
                .description(sku.getDescription())
                .weightInGrams(sku.getWeightInGrams())
                .originCountry(sku.getOriginCountry())
                .name(sku.getName())
                .gender(sku.getProduct().getGender())
                .productType(sku.getProduct().getProductType().getName())
                .department(sku.getProduct().getDepartment().getName())
                .genderList(sku.getProduct().getGenderList())
                .brand(sku.getProduct().getBrand().getName())
                .longDescription(sku.getLongDescription())
                .color(sku.getConfigurations()
                        .stream()
                        .filter(c -> c.getType()
                                .equalsIgnoreCase("color"))
                        .findFirst().orElse(new Configurations("None", "color"))
                        .getName())
                .build();
    }
}