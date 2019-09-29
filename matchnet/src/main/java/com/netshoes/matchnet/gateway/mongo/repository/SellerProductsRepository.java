package com.netshoes.matchnet.gateway.mongo.repository;

import com.netshoes.matchnet.domain.sellerProducts.SellerProducts;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

/**
 * Created by Grazeffe on 28/09/19.
 * https://github.com/Grazeffe
 */
@Repository
public interface SellerProductsRepository extends MongoRepository<SellerProducts, String> {
}