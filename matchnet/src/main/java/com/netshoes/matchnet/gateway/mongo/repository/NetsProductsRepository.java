package com.netshoes.matchnet.gateway.mongo.repository;

import com.netshoes.matchnet.domain.netsProducts.NetshoesProducts;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@Repository
public interface NetsProductsRepository extends MongoRepository<NetshoesProducts, String> {
}