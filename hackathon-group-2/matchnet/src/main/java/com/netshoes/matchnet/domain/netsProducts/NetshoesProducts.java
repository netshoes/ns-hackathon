package com.netshoes.matchnet.domain.netsProducts;

import com.netshoes.matchnet.gateway.http.json.Dimension;
import lombok.Builder;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@Builder
@Document
public class NetshoesProducts {

    @Id
    private String id;
    private Dimension dimension;
    private String description;
    private int weightInGrams;
    private String originCountry;
    private String name;
    private String gender;
    private String productType;
    private String department;
    private List<String> genderList;
    private String brand;
    private String longDescription;
    private String color;
}