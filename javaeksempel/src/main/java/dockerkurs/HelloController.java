package dockerkurs;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Random;

@SuppressWarnings("ALL")
@RestController
public class HelloController {

    @GetMapping("/")
    ResponseEntity<Integer> home() {
        System.out.println("hello");
        return ResponseEntity.ok(new Random().nextInt(100));
    }

    @PostMapping("/")
    ResponseEntity<Void> post() {
        return ResponseEntity.ok().build();
    }
}
