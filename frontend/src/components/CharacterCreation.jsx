import React, { useState } from "react";
import { createCharacter } from "../services/api";
import "./CharacterCreation.css";

const classes = [
  {
    name: "Fighter",
    armor_class: 12,
    stats: {
      Strength: 17,
      Dexterity: 13,
      Constitution: 15,
      Intelligence: 10,
      Wisdom: 12,
      Charisma: 8,
    },
    description:
      "Fighters rule many battlefields. Questing knights, royal champions, elite soldiers, and hardened mercenaries—as Fighters, they all share an unparalleled prowess with weapons and armor.",
  },
  {
    name: "Bard",
    armor_class: 13,
    stats: {
      Strength: 8,
      Dexterity: 15,
      Constitution: 13,
      Intelligence: 12,
      Wisdom: 10,
      Charisma: 17,
    },
    description:
      "Invoking magic through music, dance, and verse, Bards are expert at inspiring others, soothing hurts, disheartening foes, and creating illusions. Their life is spent traveling, gathering lore, telling stories, and living on the gratitude of audiences.",
  },
  {
    name: "Ranger",
    armor_class: 15,
    stats: {
      Strength: 12,
      Dexterity: 17,
      Constitution: 13,
      Intelligence: 8,
      Wisdom: 15,
      Charisma: 10,
    },
    description:
      "Rangers keep their unending watch in the wilderness. They learn to track their quarry as a predator does, moving stealthily through the wilds and hiding themselves in brush and rubble.",
  },
  {
    name: "Wizard",
    armor_class: 12,
    stats: {
      Strength: 8,
      Dexterity: 13,
      Constitution: 15,
      Intelligence: 17,
      Wisdom: 10,
      Charisma: 12,
    },
    description:
      "Wizards are defined by their exhaustive study of magic’s inner workings. They cast spells of explosive fire, arcing lightning, subtle deception, and spectacular transformations. Their magic conjures monsters, glimpses the future, or forms protective barriers.",
  },
  {
    name: "Rogue",
    armor_class: 14,
    stats: {
      Strength: 8,
      Dexterity: 17,
      Constitution: 14,
      Intelligence: 13,
      Wisdom: 13,
      Charisma: 10,
    },
    description:
      "Rogues rely on cunning, stealth, and exploiting their foes’ vulnerabilities. They excel in subtle strikes over brute force, preferring one precise blow to a barrage of hits.",
  },
  {
    name: "Cleric",
    armor_class: 10,
    stats: {
      Strength: 15,
      Dexterity: 10,
      Constitution: 13,
      Intelligence: 8,
      Wisdom: 17,
      Charisma: 12,
    },
    description:
      "Clerics draw power from the divine. Blessed by a deity, they harness miracles and channel divine magic to bolster allies and vanquish foes.",
  },
];

function CharacterCreation({ onCharacterCreated }) {
  const [name, setName] = useState("");

  const handleSelect = async (chosenClass) => {
    if (!name) {
      alert("Please enter a character name.");
      return;
    }
    try {
      const response = await createCharacter(name, chosenClass);
      if (response.session_id && response.player_state) {
        onCharacterCreated(response.session_id, response.player_state);
      }
    } catch (error) {
      console.error("Error creating character: ", error);
    }
  };

  return (
    <div className="character-creation-container">
      <h2>Create Your Character</h2>
      <div>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Enter character name..."
        />
      </div>
      <div className="class-list">
        {classes.map((cls) => (
          <div key={cls.name} className="class-card" onClick={() => handleSelect(cls.name)}>
            <h3>{cls.name}</h3>
            <p><strong>Armor Class:</strong> {cls.armor_class}</p>
            <ul>
              {Object.entries(cls.stats).map(([stat, value]) => (
                <li key={stat}><strong>{stat}:</strong> {value}</li>
              ))}
            </ul>
            <p>{cls.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default CharacterCreation;