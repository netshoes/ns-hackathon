package com.netshoes.matchnet.gateway.http.json;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.AllArgsConstructor;
import lombok.Data;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@Data
@JsonIgnoreProperties(ignoreUnknown = true)
@AllArgsConstructor
public class Configurations {

    private String name;
    private String type;
}