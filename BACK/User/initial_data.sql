-- Insertar roles
INSERT INTO roles (name)
VALUES
('Client'),
('Vet'),
('Admin');

-- Insertar usuarios
INSERT INTO "user" (
    email, first_name, last_name, password, address, phone, image, date_joined,
    is_active, is_staff, is_superuser, role_id
)
VALUES
('gastondicampli@gmail.com', 'Gaston', 'Di Campli', 'pbkdf2_sha256$600000$5AckuCNmyCM6lgLATnfxT8$nljFWwLfJnCPMsUYzrM2bmGsQdUNIraa18TdPPuJnmU=', '101 Oak St', '123456789', 'bob_johnson.jpg', '2024-05-23 16:00:04', TRUE, FALSE, FALSE, 1),
('cesiafiorella@gmail.com', 'Cesia', 'Fiorella', 'pbkdf2_sha256$600000$5AckuCNmyCM6lgLATnfxT8$nljFWwLfJnCPMsUYzrM2bmGsQdUNIraa18TdPPuJnmU=', '456 Main St', '123456789', 'joan_doe.jpg', '2024-05-23 16:00:04', TRUE, FALSE, FALSE, 1),
('marcovirinni@gmail.com',  'Marco', 'Virinni', 'pbkdf2_sha256$600000$5AckuCNmyCM6lgLATnfxT8$nljFWwLfJnCPMsUYzrM2bmGsQdUNIraa18TdPPuJnmU=', '123 Main St', '123456789', 'https://res.cloudinary.com/dbz5bknul/image/upload/v1710547090/marco_virinni_oov5tk.jpg', '2024-05-23 16:00:04', TRUE, TRUE, FALSE, 1),
('marialopezvet@gmail.com', 'Maria', 'Lopez', 'pbkdf2_sha256$600000$5AckuCNmyCM6lgLATnfxT8$nljFWwLfJnCPMsUYzrM2bmGsQdUNIraa18TdPPuJnmU=', '123 Main St', '123456789', 'eva_williams.jpg', '2024-05-23 16:00:04', TRUE, TRUE, FALSE, 2),
('developers-veterinarian@gmail.com','Develop', 'Team', 'pbkdf2_sha256$600000$TM6SUusGx9g4tG3ixjFULr$2D2mz/i5G1/1mEx4bhuIm6NKwPqmg3ZafjD0KD9SLFA=', 'localhost', '123456789', 'michael_brown.jpg', '2024-05-23 16:00:04', TRUE, TRUE, TRUE, 3);
