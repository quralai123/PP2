CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INT;
BEGIN
    SELECT id INTO v_contact_id
    FROM contacts
    WHERE name = p_contact_name
    LIMIT 1;

    IF v_contact_id IS NULL THEN
        RAISE NOTICE 'Contact not found: %', p_contact_name;
        RETURN;
    END IF;

    INSERT INTO phones (contact_id, number, type)
    VALUES (v_contact_id, p_phone, p_type)
    ON CONFLICT DO NOTHING;

END;
$$;


CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INT;
    v_group_id INT;
BEGIN
    SELECT id INTO v_contact_id
    FROM contacts
    WHERE name = p_contact_name
    LIMIT 1;

    IF v_contact_id IS NULL THEN
        RAISE NOTICE 'Contact not found: %', p_contact_name;
        RETURN;
    END IF;

    SELECT id INTO v_group_id
    FROM groups
    WHERE name = p_group_name;

    IF v_group_id IS NULL THEN
        INSERT INTO groups(name)
        VALUES (p_group_name)
        RETURNING id INTO v_group_id;
    END IF;

    UPDATE contacts
    SET group_id = v_group_id
    WHERE id = v_contact_id;

END;
$$;