package com.netshoes.matchnet.modulos.separator.gateway.http;

import com.netshoes.matchnet.modulos.separator.usecase.SmartSeparator;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by Grazeffe on 29/09/19.
 * https://github.com/Grazeffe
 */
@RestController
@RequestMapping(value = "/smart-separator",
        produces = MediaType.APPLICATION_JSON_VALUE)
@RequiredArgsConstructor
@Slf4j
public class SmartSeparatorController {

    private final SmartSeparator smartSeparator;

    @GetMapping
    public ResponseEntity<?> importSeller() {
        try {
            return ResponseEntity.ok(smartSeparator.execute());
        } catch (Exception ex) {
            log.error(ex.getMessage());
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Ocorreu algum erro para processar os dados!");
        }
    }
}