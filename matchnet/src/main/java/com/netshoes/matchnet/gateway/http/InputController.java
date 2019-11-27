package com.netshoes.matchnet.gateway.http;

import com.netshoes.matchnet.domain.sellerProducts.SellerProducts;
import com.netshoes.matchnet.gateway.http.json.SkuNets;
import com.netshoes.matchnet.modulos.input.usecase.InputingData;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * Created by Grazeffe on 28/09/19.
 * https://github.com/Grazeffe
 */
@RestController
@RequestMapping(value = "/input",
        produces = MediaType.APPLICATION_JSON_VALUE)
@RequiredArgsConstructor
public class InputController {

    private final InputingData inputingData;

    @PostMapping("/import-seller-products")
    public ResponseEntity<?> importSeller(@RequestBody final List<SellerProducts> sellerProducts) {
        try {
            inputingData.inputSellerProducts(sellerProducts);
            return ResponseEntity.accepted().body("Done!");
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Ocorreu algum para importar os dados!");
        }
    }

    @PostMapping(value = "/import-nets-products",
            consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<?> importNets(@RequestBody final List<SkuNets> netsProducts) {
        try {
            inputingData.inputNetsProducts(netsProducts);
            return ResponseEntity.accepted().body("Done!");
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Ocorreu algum para importar os dados!");
        }
    }
}