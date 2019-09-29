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
public class Product {

    private String gender;
    private ProductType productType;
    private Department department;
    private List<String> genderList;
    private Brand brand;
}