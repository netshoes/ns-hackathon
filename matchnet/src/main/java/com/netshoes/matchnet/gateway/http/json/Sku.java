package com.netshoes.matchnet.gateway.http.json;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;

import java.util.List;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@Data
@JsonIgnoreProperties(ignoreUnknown = true)
public class Sku {
    private Dimension dimension;
    @org.springframework.data.annotation.Id
    private Id id;
    private String merchandiseOrigin;
    private String description;
    private int weightInGrams;
    private String originCountry;
    private String name;
    private Product product;
    private String longDescription;
    private List<Configurations> configurations;
}