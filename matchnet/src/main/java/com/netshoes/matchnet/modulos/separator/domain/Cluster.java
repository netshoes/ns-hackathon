package com.netshoes.matchnet.modulos.separator.domain;

import lombok.Data;
import org.springframework.data.mongodb.core.mapping.Document;

/**
 * Created by Grazeffe on 28/09/19.
 * https://github.com/Grazeffe
 */
@Data
@Document
public class Cluster {

    private String cluster;
    private String distancia;
}