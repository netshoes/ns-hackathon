package com.netshoes.matchnet;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.openfeign.EnableFeignClients;

@EnableFeignClients
@SpringBootApplication
public class MatchnetApplication {

	public static void main(String[] args) {
		SpringApplication.run(MatchnetApplication.class, args);
	}
}