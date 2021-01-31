
# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 491 | 479 | 12 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| ta366 |  72 | 71 | 1 | Hardware |
| up522 |  50 | 48 | 2 | Hardware, BGP |
| ta368 |  80 | 79 | 1 | Hardware |
| smv462 |  56 | 55 | 1 | Hardware |
| ta373 |  71 | 70 | 1 | Hardware |
| cmp308 |  87 | 82 | 5 | Hardware |
| ta367 |  75 | 74 | 1 | Hardware |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| Hardware |  408 | 397 | 11 |
| NTP |  7 | 7 | 0 |
| Interface State |  22 | 22 | 0 |
| LLDP Topology |  22 | 22 | 0 |
| IP Reachability |  18 | 18 | 0 |
| BGP |  7 | 6 | 1 |
| Reload Cause |  7 | 7 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 2 | ta366 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 4 | up522 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 6 | ta368 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 8 | smv462 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 10 | ta373 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 14 | cmp308 | Hardware | Power supply state | Power supply 5 | FAIL | Power supply state is "powerLoss" |
| 15 | cmp308 | Hardware | Power supply state | Power supply 4 | FAIL | Power supply state is "powerLoss" |
| 16 | cmp308 | Hardware | Power supply state | Power supply 6 | FAIL | Power supply state is "powerLoss" |
| 18 | ta367 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 35 | cmp308 | Hardware | fan status (power supplies) | PowerSupply7 | FAIL | fan status is "notInserted" |
| 36 | cmp308 | Hardware | fan status (power supplies) | PowerSupply8 | FAIL | fan status is "notInserted" |
| 479 | up522 | BGP | ArBGP is configured and operating | ArBGP | FAIL | Operating routing protocol model: ribd |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | ta366 | Hardware | Power supply state | Power supply 1 | PASS |  |
| 2 | ta366 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 3 | up522 | Hardware | Power supply state | Power supply 1 | PASS |  |
| 4 | up522 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 5 | ta368 | Hardware | Power supply state | Power supply 1 | PASS |  |
| 6 | ta368 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 7 | smv462 | Hardware | Power supply state | Power supply 1 | PASS |  |
| 8 | smv462 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 9 | ta373 | Hardware | Power supply state | Power supply 1 | PASS |  |
| 10 | ta373 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 11 | cmp308 | Hardware | Power supply state | Power supply 1 | PASS |  |
| 12 | cmp308 | Hardware | Power supply state | Power supply 3 | PASS |  |
| 13 | cmp308 | Hardware | Power supply state | Power supply 2 | PASS |  |
| 14 | cmp308 | Hardware | Power supply state | Power supply 5 | FAIL | Power supply state is "powerLoss" |
| 15 | cmp308 | Hardware | Power supply state | Power supply 4 | FAIL | Power supply state is "powerLoss" |
| 16 | cmp308 | Hardware | Power supply state | Power supply 6 | FAIL | Power supply state is "powerLoss" |
| 17 | ta367 | Hardware | Power supply state | Power supply 1 | PASS |  |
| 18 | ta367 | Hardware | Power supply state | Power supply 2 | FAIL | Power supply state is "powerLoss" |
| 19 | ta366 | Hardware | fan status (power supplies) | PowerSupply1 | PASS |  |
| 20 | ta366 | Hardware | fan status (power supplies) | PowerSupply2 | PASS |  |
| 21 | up522 | Hardware | fan status (power supplies) | PowerSupply1 | PASS |  |
| 22 | up522 | Hardware | fan status (power supplies) | PowerSupply2 | PASS |  |
| 23 | ta368 | Hardware | fan status (power supplies) | PowerSupply1 | PASS |  |
| 24 | ta368 | Hardware | fan status (power supplies) | PowerSupply2 | PASS |  |
| 25 | smv462 | Hardware | fan status (power supplies) | PowerSupply1 | PASS |  |
| 26 | smv462 | Hardware | fan status (power supplies) | PowerSupply2 | PASS |  |
| 27 | ta373 | Hardware | fan status (power supplies) | PowerSupply1 | PASS |  |
| 28 | ta373 | Hardware | fan status (power supplies) | PowerSupply2 | PASS |  |
| 29 | cmp308 | Hardware | fan status (power supplies) | PowerSupply1 | PASS |  |
| 30 | cmp308 | Hardware | fan status (power supplies) | PowerSupply2 | PASS |  |
| 31 | cmp308 | Hardware | fan status (power supplies) | PowerSupply3 | PASS |  |
| 32 | cmp308 | Hardware | fan status (power supplies) | PowerSupply4 | PASS |  |
| 33 | cmp308 | Hardware | fan status (power supplies) | PowerSupply5 | PASS |  |
| 34 | cmp308 | Hardware | fan status (power supplies) | PowerSupply6 | PASS |  |
| 35 | cmp308 | Hardware | fan status (power supplies) | PowerSupply7 | FAIL | fan status is "notInserted" |
| 36 | cmp308 | Hardware | fan status (power supplies) | PowerSupply8 | FAIL | fan status is "notInserted" |
| 37 | ta367 | Hardware | fan status (power supplies) | PowerSupply1 | PASS |  |
| 38 | ta367 | Hardware | fan status (power supplies) | PowerSupply2 | PASS |  |
| 39 | ta366 | Hardware | fan status (fan tray) | Tray 1 | PASS |  |
| 40 | ta366 | Hardware | fan status (fan tray) | Tray 2 | PASS |  |
| 41 | ta366 | Hardware | fan status (fan tray) | Tray 3 | PASS |  |
| 42 | ta366 | Hardware | fan status (fan tray) | Tray 4 | PASS |  |
| 43 | up522 | Hardware | fan status (fan tray) | Tray 1 | PASS |  |
| 44 | up522 | Hardware | fan status (fan tray) | Tray 2 | PASS |  |
| 45 | up522 | Hardware | fan status (fan tray) | Tray 3 | PASS |  |
| 46 | up522 | Hardware | fan status (fan tray) | Tray 4 | PASS |  |
| 47 | ta368 | Hardware | fan status (fan tray) | Tray 1 | PASS |  |
| 48 | ta368 | Hardware | fan status (fan tray) | Tray 2 | PASS |  |
| 49 | ta368 | Hardware | fan status (fan tray) | Tray 3 | PASS |  |
| 50 | ta368 | Hardware | fan status (fan tray) | Tray 4 | PASS |  |
| 51 | smv462 | Hardware | fan status (fan tray) | Tray 1 | PASS |  |
| 52 | smv462 | Hardware | fan status (fan tray) | Tray 2 | PASS |  |
| 53 | smv462 | Hardware | fan status (fan tray) | Tray 3 | PASS |  |
| 54 | ta373 | Hardware | fan status (fan tray) | Tray 1 | PASS |  |
| 55 | ta373 | Hardware | fan status (fan tray) | Tray 2 | PASS |  |
| 56 | ta373 | Hardware | fan status (fan tray) | Tray 3 | PASS |  |
| 57 | ta373 | Hardware | fan status (fan tray) | Tray 4 | PASS |  |
| 58 | cmp308 | Hardware | fan status (fan tray) | Tray 1 | PASS |  |
| 59 | cmp308 | Hardware | fan status (fan tray) | Tray 2 | PASS |  |
| 60 | cmp308 | Hardware | fan status (fan tray) | Tray 3 | PASS |  |
| 61 | cmp308 | Hardware | fan status (fan tray) | Tray 4 | PASS |  |
| 62 | cmp308 | Hardware | fan status (fan tray) | Tray 5 | PASS |  |
| 63 | cmp308 | Hardware | fan status (fan tray) | Tray 6 | PASS |  |
| 64 | ta367 | Hardware | fan status (fan tray) | Tray 1 | PASS |  |
| 65 | ta367 | Hardware | fan status (fan tray) | Tray 2 | PASS |  |
| 66 | ta367 | Hardware | fan status (fan tray) | Tray 3 | PASS |  |
| 67 | ta367 | Hardware | fan status (fan tray) | Tray 4 | PASS |  |
| 68 | ta366 | Hardware | temperature | system temperature | PASS |  |
| 69 | up522 | Hardware | temperature | system temperature | PASS |  |
| 70 | ta368 | Hardware | temperature | system temperature | PASS |  |
| 71 | smv462 | Hardware | temperature | system temperature | PASS |  |
| 72 | ta373 | Hardware | temperature | system temperature | PASS |  |
| 73 | cmp308 | Hardware | temperature | system temperature | PASS |  |
| 74 | ta367 | Hardware | temperature | system temperature | PASS |  |
| 75 | ta366 | Hardware | transceivers manufacturers | port 30 | PASS |  |
| 76 | ta366 | Hardware | transceivers manufacturers | port 28 | PASS |  |
| 77 | ta366 | Hardware | transceivers manufacturers | port 29 | PASS |  |
| 78 | ta366 | Hardware | transceivers manufacturers | port 35 | PASS |  |
| 79 | ta366 | Hardware | transceivers manufacturers | port 34 | PASS |  |
| 80 | ta366 | Hardware | transceivers manufacturers | port 24 | PASS |  |
| 81 | ta366 | Hardware | transceivers manufacturers | port 25 | PASS |  |
| 82 | ta366 | Hardware | transceivers manufacturers | port 26 | PASS |  |
| 83 | ta366 | Hardware | transceivers manufacturers | port 27 | PASS |  |
| 84 | ta366 | Hardware | transceivers manufacturers | port 20 | PASS |  |
| 85 | ta366 | Hardware | transceivers manufacturers | port 21 | PASS |  |
| 86 | ta366 | Hardware | transceivers manufacturers | port 22 | PASS |  |
| 87 | ta366 | Hardware | transceivers manufacturers | port 23 | PASS |  |
| 88 | ta366 | Hardware | transceivers manufacturers | port 46 | PASS |  |
| 89 | ta366 | Hardware | transceivers manufacturers | port 47 | PASS |  |
| 90 | ta366 | Hardware | transceivers manufacturers | port 44 | PASS |  |
| 91 | ta366 | Hardware | transceivers manufacturers | port 45 | PASS |  |
| 92 | ta366 | Hardware | transceivers manufacturers | port 42 | PASS |  |
| 93 | ta366 | Hardware | transceivers manufacturers | port 43 | PASS |  |
| 94 | ta366 | Hardware | transceivers manufacturers | port 40 | PASS |  |
| 95 | ta366 | Hardware | transceivers manufacturers | port 41 | PASS |  |
| 96 | ta366 | Hardware | transceivers manufacturers | port 1 | PASS |  |
| 97 | ta366 | Hardware | transceivers manufacturers | port 3 | PASS |  |
| 98 | ta366 | Hardware | transceivers manufacturers | port 2 | PASS |  |
| 99 | ta366 | Hardware | transceivers manufacturers | port 5 | PASS |  |
| 100 | ta366 | Hardware | transceivers manufacturers | port 4 | PASS |  |
| 101 | ta366 | Hardware | transceivers manufacturers | port 7 | PASS |  |
| 102 | ta366 | Hardware | transceivers manufacturers | port 6 | PASS |  |
| 103 | ta366 | Hardware | transceivers manufacturers | port 9 | PASS |  |
| 104 | ta366 | Hardware | transceivers manufacturers | port 8 | PASS |  |
| 105 | ta366 | Hardware | transceivers manufacturers | port 18 | PASS |  |
| 106 | ta366 | Hardware | transceivers manufacturers | port 13 | PASS |  |
| 107 | ta366 | Hardware | transceivers manufacturers | port 38 | PASS |  |
| 108 | ta366 | Hardware | transceivers manufacturers | port 14 | PASS |  |
| 109 | ta366 | Hardware | transceivers manufacturers | port 11 | PASS |  |
| 110 | ta366 | Hardware | transceivers manufacturers | port 10 | PASS |  |
| 111 | ta366 | Hardware | transceivers manufacturers | port 39 | PASS |  |
| 112 | ta366 | Hardware | transceivers manufacturers | port 12 | PASS |  |
| 113 | ta366 | Hardware | transceivers manufacturers | port 15 | PASS |  |
| 114 | ta366 | Hardware | transceivers manufacturers | port 48 | PASS |  |
| 115 | ta366 | Hardware | transceivers manufacturers | port 17 | PASS |  |
| 116 | ta366 | Hardware | transceivers manufacturers | port 16 | PASS |  |
| 117 | ta366 | Hardware | transceivers manufacturers | port 19 | PASS |  |
| 118 | ta366 | Hardware | transceivers manufacturers | port 54 | PASS |  |
| 119 | ta366 | Hardware | transceivers manufacturers | port 31 | PASS |  |
| 120 | ta366 | Hardware | transceivers manufacturers | port 49 | PASS |  |
| 121 | ta366 | Hardware | transceivers manufacturers | port 51 | PASS |  |
| 122 | ta366 | Hardware | transceivers manufacturers | port 36 | PASS |  |
| 123 | ta366 | Hardware | transceivers manufacturers | port 53 | PASS |  |
| 124 | ta366 | Hardware | transceivers manufacturers | port 52 | PASS |  |
| 125 | ta366 | Hardware | transceivers manufacturers | port 33 | PASS |  |
| 126 | ta366 | Hardware | transceivers manufacturers | port 37 | PASS |  |
| 127 | ta366 | Hardware | transceivers manufacturers | port 32 | PASS |  |
| 128 | ta366 | Hardware | transceivers manufacturers | port 50 | PASS |  |
| 129 | up522 | Hardware | transceivers manufacturers | port 11 | PASS |  |
| 130 | up522 | Hardware | transceivers manufacturers | port 10 | PASS |  |
| 131 | up522 | Hardware | transceivers manufacturers | port 6 | PASS |  |
| 132 | up522 | Hardware | transceivers manufacturers | port 13 | PASS |  |
| 133 | up522 | Hardware | transceivers manufacturers | port 12 | PASS |  |
| 134 | up522 | Hardware | transceivers manufacturers | port 17 | PASS |  |
| 135 | up522 | Hardware | transceivers manufacturers | port 15 | PASS |  |
| 136 | up522 | Hardware | transceivers manufacturers | port 23 | PASS |  |
| 137 | up522 | Hardware | transceivers manufacturers | port 24 | PASS |  |
| 138 | up522 | Hardware | transceivers manufacturers | port 25 | PASS |  |
| 139 | up522 | Hardware | transceivers manufacturers | port 26 | PASS |  |
| 140 | up522 | Hardware | transceivers manufacturers | port 27 | PASS |  |
| 141 | up522 | Hardware | transceivers manufacturers | port 20 | PASS |  |
| 142 | up522 | Hardware | transceivers manufacturers | port 21 | PASS |  |
| 143 | up522 | Hardware | transceivers manufacturers | port 22 | PASS |  |
| 144 | up522 | Hardware | transceivers manufacturers | port 16 | PASS |  |
| 145 | up522 | Hardware | transceivers manufacturers | port 19 | PASS |  |
| 146 | up522 | Hardware | transceivers manufacturers | port 32 | PASS |  |
| 147 | up522 | Hardware | transceivers manufacturers | port 31 | PASS |  |
| 148 | up522 | Hardware | transceivers manufacturers | port 30 | PASS |  |
| 149 | up522 | Hardware | transceivers manufacturers | port 28 | PASS |  |
| 150 | up522 | Hardware | transceivers manufacturers | port 29 | PASS |  |
| 151 | up522 | Hardware | transceivers manufacturers | port 34 | PASS |  |
| 152 | up522 | Hardware | transceivers manufacturers | port 1 | PASS |  |
| 153 | up522 | Hardware | transceivers manufacturers | port 33 | PASS |  |
| 154 | up522 | Hardware | transceivers manufacturers | port 3 | PASS |  |
| 155 | up522 | Hardware | transceivers manufacturers | port 2 | PASS |  |
| 156 | up522 | Hardware | transceivers manufacturers | port 5 | PASS |  |
| 157 | up522 | Hardware | transceivers manufacturers | port 4 | PASS |  |
| 158 | up522 | Hardware | transceivers manufacturers | port 7 | PASS |  |
| 159 | up522 | Hardware | transceivers manufacturers | port 18 | PASS |  |
| 160 | up522 | Hardware | transceivers manufacturers | port 9 | PASS |  |
| 161 | up522 | Hardware | transceivers manufacturers | port 8 | PASS |  |
| 162 | up522 | Hardware | transceivers manufacturers | port 14 | PASS |  |
| 163 | ta368 | Hardware | transceivers manufacturers | port 30 | PASS |  |
| 164 | ta368 | Hardware | transceivers manufacturers | port 28 | PASS |  |
| 165 | ta368 | Hardware | transceivers manufacturers | port 29 | PASS |  |
| 166 | ta368 | Hardware | transceivers manufacturers | port 35 | PASS |  |
| 167 | ta368 | Hardware | transceivers manufacturers | port 34 | PASS |  |
| 168 | ta368 | Hardware | transceivers manufacturers | port 24 | PASS |  |
| 169 | ta368 | Hardware | transceivers manufacturers | port 25 | PASS |  |
| 170 | ta368 | Hardware | transceivers manufacturers | port 26 | PASS |  |
| 171 | ta368 | Hardware | transceivers manufacturers | port 27 | PASS |  |
| 172 | ta368 | Hardware | transceivers manufacturers | port 20 | PASS |  |
| 173 | ta368 | Hardware | transceivers manufacturers | port 21 | PASS |  |
| 174 | ta368 | Hardware | transceivers manufacturers | port 22 | PASS |  |
| 175 | ta368 | Hardware | transceivers manufacturers | port 23 | PASS |  |
| 176 | ta368 | Hardware | transceivers manufacturers | port 46 | PASS |  |
| 177 | ta368 | Hardware | transceivers manufacturers | port 47 | PASS |  |
| 178 | ta368 | Hardware | transceivers manufacturers | port 44 | PASS |  |
| 179 | ta368 | Hardware | transceivers manufacturers | port 45 | PASS |  |
| 180 | ta368 | Hardware | transceivers manufacturers | port 42 | PASS |  |
| 181 | ta368 | Hardware | transceivers manufacturers | port 43 | PASS |  |
| 182 | ta368 | Hardware | transceivers manufacturers | port 40 | PASS |  |
| 183 | ta368 | Hardware | transceivers manufacturers | port 41 | PASS |  |
| 184 | ta368 | Hardware | transceivers manufacturers | port 1 | PASS |  |
| 185 | ta368 | Hardware | transceivers manufacturers | port 3 | PASS |  |
| 186 | ta368 | Hardware | transceivers manufacturers | port 2 | PASS |  |
| 187 | ta368 | Hardware | transceivers manufacturers | port 5 | PASS |  |
| 188 | ta368 | Hardware | transceivers manufacturers | port 4 | PASS |  |
| 189 | ta368 | Hardware | transceivers manufacturers | port 7 | PASS |  |
| 190 | ta368 | Hardware | transceivers manufacturers | port 6 | PASS |  |
| 191 | ta368 | Hardware | transceivers manufacturers | port 9 | PASS |  |
| 192 | ta368 | Hardware | transceivers manufacturers | port 8 | PASS |  |
| 193 | ta368 | Hardware | transceivers manufacturers | port 18 | PASS |  |
| 194 | ta368 | Hardware | transceivers manufacturers | port 13 | PASS |  |
| 195 | ta368 | Hardware | transceivers manufacturers | port 38 | PASS |  |
| 196 | ta368 | Hardware | transceivers manufacturers | port 14 | PASS |  |
| 197 | ta368 | Hardware | transceivers manufacturers | port 11 | PASS |  |
| 198 | ta368 | Hardware | transceivers manufacturers | port 10 | PASS |  |
| 199 | ta368 | Hardware | transceivers manufacturers | port 39 | PASS |  |
| 200 | ta368 | Hardware | transceivers manufacturers | port 12 | PASS |  |
| 201 | ta368 | Hardware | transceivers manufacturers | port 15 | PASS |  |
| 202 | ta368 | Hardware | transceivers manufacturers | port 48 | PASS |  |
| 203 | ta368 | Hardware | transceivers manufacturers | port 17 | PASS |  |
| 204 | ta368 | Hardware | transceivers manufacturers | port 16 | PASS |  |
| 205 | ta368 | Hardware | transceivers manufacturers | port 19 | PASS |  |
| 206 | ta368 | Hardware | transceivers manufacturers | port 54 | PASS |  |
| 207 | ta368 | Hardware | transceivers manufacturers | port 31 | PASS |  |
| 208 | ta368 | Hardware | transceivers manufacturers | port 49 | PASS |  |
| 209 | ta368 | Hardware | transceivers manufacturers | port 51 | PASS |  |
| 210 | ta368 | Hardware | transceivers manufacturers | port 36 | PASS |  |
| 211 | ta368 | Hardware | transceivers manufacturers | port 53 | PASS |  |
| 212 | ta368 | Hardware | transceivers manufacturers | port 52 | PASS |  |
| 213 | ta368 | Hardware | transceivers manufacturers | port 33 | PASS |  |
| 214 | ta368 | Hardware | transceivers manufacturers | port 37 | PASS |  |
| 215 | ta368 | Hardware | transceivers manufacturers | port 32 | PASS |  |
| 216 | ta368 | Hardware | transceivers manufacturers | port 50 | PASS |  |
| 217 | smv462 | Hardware | transceivers manufacturers | port 11 | PASS |  |
| 218 | smv462 | Hardware | transceivers manufacturers | port 10 | PASS |  |
| 219 | smv462 | Hardware | transceivers manufacturers | port 6 | PASS |  |
| 220 | smv462 | Hardware | transceivers manufacturers | port 13 | PASS |  |
| 221 | smv462 | Hardware | transceivers manufacturers | port 29 | PASS |  |
| 222 | smv462 | Hardware | transceivers manufacturers | port 12 | PASS |  |
| 223 | smv462 | Hardware | transceivers manufacturers | port 17 | PASS |  |
| 224 | smv462 | Hardware | transceivers manufacturers | port 15 | PASS |  |
| 225 | smv462 | Hardware | transceivers manufacturers | port 23 | PASS |  |
| 226 | smv462 | Hardware | transceivers manufacturers | port 24 | PASS |  |
| 227 | smv462 | Hardware | transceivers manufacturers | port 25 | PASS |  |
| 228 | smv462 | Hardware | transceivers manufacturers | port 26 | PASS |  |
| 229 | smv462 | Hardware | transceivers manufacturers | port 27 | PASS |  |
| 230 | smv462 | Hardware | transceivers manufacturers | port 20 | PASS |  |
| 231 | smv462 | Hardware | transceivers manufacturers | port 21 | PASS |  |
| 232 | smv462 | Hardware | transceivers manufacturers | port 22 | PASS |  |
| 233 | smv462 | Hardware | transceivers manufacturers | port 16 | PASS |  |
| 234 | smv462 | Hardware | transceivers manufacturers | port 19 | PASS |  |
| 235 | smv462 | Hardware | transceivers manufacturers | port 32 | PASS |  |
| 236 | smv462 | Hardware | transceivers manufacturers | port 31 | PASS |  |
| 237 | smv462 | Hardware | transceivers manufacturers | port 30 | PASS |  |
| 238 | smv462 | Hardware | transceivers manufacturers | port 28 | PASS |  |
| 239 | smv462 | Hardware | transceivers manufacturers | port 36 | PASS |  |
| 240 | smv462 | Hardware | transceivers manufacturers | port 35 | PASS |  |
| 241 | smv462 | Hardware | transceivers manufacturers | port 34 | PASS |  |
| 242 | smv462 | Hardware | transceivers manufacturers | port 1 | PASS |  |
| 243 | smv462 | Hardware | transceivers manufacturers | port 33 | PASS |  |
| 244 | smv462 | Hardware | transceivers manufacturers | port 3 | PASS |  |
| 245 | smv462 | Hardware | transceivers manufacturers | port 2 | PASS |  |
| 246 | smv462 | Hardware | transceivers manufacturers | port 5 | PASS |  |
| 247 | smv462 | Hardware | transceivers manufacturers | port 4 | PASS |  |
| 248 | smv462 | Hardware | transceivers manufacturers | port 7 | PASS |  |
| 249 | smv462 | Hardware | transceivers manufacturers | port 18 | PASS |  |
| 250 | smv462 | Hardware | transceivers manufacturers | port 9 | PASS |  |
| 251 | smv462 | Hardware | transceivers manufacturers | port 8 | PASS |  |
| 252 | smv462 | Hardware | transceivers manufacturers | port 14 | PASS |  |
| 253 | ta373 | Hardware | transceivers manufacturers | port 30 | PASS |  |
| 254 | ta373 | Hardware | transceivers manufacturers | port 28 | PASS |  |
| 255 | ta373 | Hardware | transceivers manufacturers | port 29 | PASS |  |
| 256 | ta373 | Hardware | transceivers manufacturers | port 35 | PASS |  |
| 257 | ta373 | Hardware | transceivers manufacturers | port 34 | PASS |  |
| 258 | ta373 | Hardware | transceivers manufacturers | port 24 | PASS |  |
| 259 | ta373 | Hardware | transceivers manufacturers | port 25 | PASS |  |
| 260 | ta373 | Hardware | transceivers manufacturers | port 26 | PASS |  |
| 261 | ta373 | Hardware | transceivers manufacturers | port 27 | PASS |  |
| 262 | ta373 | Hardware | transceivers manufacturers | port 20 | PASS |  |
| 263 | ta373 | Hardware | transceivers manufacturers | port 21 | PASS |  |
| 264 | ta373 | Hardware | transceivers manufacturers | port 22 | PASS |  |
| 265 | ta373 | Hardware | transceivers manufacturers | port 23 | PASS |  |
| 266 | ta373 | Hardware | transceivers manufacturers | port 46 | PASS |  |
| 267 | ta373 | Hardware | transceivers manufacturers | port 47 | PASS |  |
| 268 | ta373 | Hardware | transceivers manufacturers | port 44 | PASS |  |
| 269 | ta373 | Hardware | transceivers manufacturers | port 45 | PASS |  |
| 270 | ta373 | Hardware | transceivers manufacturers | port 42 | PASS |  |
| 271 | ta373 | Hardware | transceivers manufacturers | port 43 | PASS |  |
| 272 | ta373 | Hardware | transceivers manufacturers | port 40 | PASS |  |
| 273 | ta373 | Hardware | transceivers manufacturers | port 41 | PASS |  |
| 274 | ta373 | Hardware | transceivers manufacturers | port 1 | PASS |  |
| 275 | ta373 | Hardware | transceivers manufacturers | port 3 | PASS |  |
| 276 | ta373 | Hardware | transceivers manufacturers | port 2 | PASS |  |
| 277 | ta373 | Hardware | transceivers manufacturers | port 5 | PASS |  |
| 278 | ta373 | Hardware | transceivers manufacturers | port 4 | PASS |  |
| 279 | ta373 | Hardware | transceivers manufacturers | port 7 | PASS |  |
| 280 | ta373 | Hardware | transceivers manufacturers | port 6 | PASS |  |
| 281 | ta373 | Hardware | transceivers manufacturers | port 9 | PASS |  |
| 282 | ta373 | Hardware | transceivers manufacturers | port 8 | PASS |  |
| 283 | ta373 | Hardware | transceivers manufacturers | port 18 | PASS |  |
| 284 | ta373 | Hardware | transceivers manufacturers | port 13 | PASS |  |
| 285 | ta373 | Hardware | transceivers manufacturers | port 38 | PASS |  |
| 286 | ta373 | Hardware | transceivers manufacturers | port 14 | PASS |  |
| 287 | ta373 | Hardware | transceivers manufacturers | port 11 | PASS |  |
| 288 | ta373 | Hardware | transceivers manufacturers | port 10 | PASS |  |
| 289 | ta373 | Hardware | transceivers manufacturers | port 39 | PASS |  |
| 290 | ta373 | Hardware | transceivers manufacturers | port 12 | PASS |  |
| 291 | ta373 | Hardware | transceivers manufacturers | port 15 | PASS |  |
| 292 | ta373 | Hardware | transceivers manufacturers | port 48 | PASS |  |
| 293 | ta373 | Hardware | transceivers manufacturers | port 17 | PASS |  |
| 294 | ta373 | Hardware | transceivers manufacturers | port 16 | PASS |  |
| 295 | ta373 | Hardware | transceivers manufacturers | port 19 | PASS |  |
| 296 | ta373 | Hardware | transceivers manufacturers | port 54 | PASS |  |
| 297 | ta373 | Hardware | transceivers manufacturers | port 31 | PASS |  |
| 298 | ta373 | Hardware | transceivers manufacturers | port 49 | PASS |  |
| 299 | ta373 | Hardware | transceivers manufacturers | port 51 | PASS |  |
| 300 | ta373 | Hardware | transceivers manufacturers | port 36 | PASS |  |
| 301 | ta373 | Hardware | transceivers manufacturers | port 53 | PASS |  |
| 302 | ta373 | Hardware | transceivers manufacturers | port 52 | PASS |  |
| 303 | ta373 | Hardware | transceivers manufacturers | port 33 | PASS |  |
| 304 | ta373 | Hardware | transceivers manufacturers | port 37 | PASS |  |
| 305 | ta373 | Hardware | transceivers manufacturers | port 32 | PASS |  |
| 306 | ta373 | Hardware | transceivers manufacturers | port 50 | PASS |  |
| 307 | cmp308 | Hardware | transceivers manufacturers | port 3/37 | PASS |  |
| 308 | cmp308 | Hardware | transceivers manufacturers | port 3/36 | PASS |  |
| 309 | cmp308 | Hardware | transceivers manufacturers | port 3/35 | PASS |  |
| 310 | cmp308 | Hardware | transceivers manufacturers | port 3/34 | PASS |  |
| 311 | cmp308 | Hardware | transceivers manufacturers | port 3/19 | PASS |  |
| 312 | cmp308 | Hardware | transceivers manufacturers | port 3/18 | PASS |  |
| 313 | cmp308 | Hardware | transceivers manufacturers | port 3/31 | PASS |  |
| 314 | cmp308 | Hardware | transceivers manufacturers | port 3/30 | PASS |  |
| 315 | cmp308 | Hardware | transceivers manufacturers | port 3/15 | PASS |  |
| 316 | cmp308 | Hardware | transceivers manufacturers | port 3/14 | PASS |  |
| 317 | cmp308 | Hardware | transceivers manufacturers | port 3/17 | PASS |  |
| 318 | cmp308 | Hardware | transceivers manufacturers | port 3/16 | PASS |  |
| 319 | cmp308 | Hardware | transceivers manufacturers | port 3/11 | PASS |  |
| 320 | cmp308 | Hardware | transceivers manufacturers | port 3/10 | PASS |  |
| 321 | cmp308 | Hardware | transceivers manufacturers | port 3/13 | PASS |  |
| 322 | cmp308 | Hardware | transceivers manufacturers | port 3/12 | PASS |  |
| 323 | cmp308 | Hardware | transceivers manufacturers | port 3/33 | PASS |  |
| 324 | cmp308 | Hardware | transceivers manufacturers | port 3/32 | PASS |  |
| 325 | cmp308 | Hardware | transceivers manufacturers | port 3/46 | PASS |  |
| 326 | cmp308 | Hardware | transceivers manufacturers | port 3/47 | PASS |  |
| 327 | cmp308 | Hardware | transceivers manufacturers | port 3/44 | PASS |  |
| 328 | cmp308 | Hardware | transceivers manufacturers | port 3/45 | PASS |  |
| 329 | cmp308 | Hardware | transceivers manufacturers | port 3/42 | PASS |  |
| 330 | cmp308 | Hardware | transceivers manufacturers | port 3/43 | PASS |  |
| 331 | cmp308 | Hardware | transceivers manufacturers | port 3/40 | PASS |  |
| 332 | cmp308 | Hardware | transceivers manufacturers | port 3/41 | PASS |  |
| 333 | cmp308 | Hardware | transceivers manufacturers | port 3/48 | PASS |  |
| 334 | cmp308 | Hardware | transceivers manufacturers | port 3/24 | PASS |  |
| 335 | cmp308 | Hardware | transceivers manufacturers | port 3/25 | PASS |  |
| 336 | cmp308 | Hardware | transceivers manufacturers | port 3/26 | PASS |  |
| 337 | cmp308 | Hardware | transceivers manufacturers | port 3/27 | PASS |  |
| 338 | cmp308 | Hardware | transceivers manufacturers | port 3/20 | PASS |  |
| 339 | cmp308 | Hardware | transceivers manufacturers | port 3/21 | PASS |  |
| 340 | cmp308 | Hardware | transceivers manufacturers | port 3/22 | PASS |  |
| 341 | cmp308 | Hardware | transceivers manufacturers | port 3/23 | PASS |  |
| 342 | cmp308 | Hardware | transceivers manufacturers | port 3/28 | PASS |  |
| 343 | cmp308 | Hardware | transceivers manufacturers | port 3/29 | PASS |  |
| 344 | cmp308 | Hardware | transceivers manufacturers | port 3/1 | PASS |  |
| 345 | cmp308 | Hardware | transceivers manufacturers | port 3/3 | PASS |  |
| 346 | cmp308 | Hardware | transceivers manufacturers | port 3/2 | PASS |  |
| 347 | cmp308 | Hardware | transceivers manufacturers | port 3/5 | PASS |  |
| 348 | cmp308 | Hardware | transceivers manufacturers | port 3/39 | PASS |  |
| 349 | cmp308 | Hardware | transceivers manufacturers | port 3/7 | PASS |  |
| 350 | cmp308 | Hardware | transceivers manufacturers | port 3/6 | PASS |  |
| 351 | cmp308 | Hardware | transceivers manufacturers | port 3/9 | PASS |  |
| 352 | cmp308 | Hardware | transceivers manufacturers | port 3/8 | PASS |  |
| 353 | cmp308 | Hardware | transceivers manufacturers | port 3/38 | PASS |  |
| 354 | cmp308 | Hardware | transceivers manufacturers | port 3/4 | PASS |  |
| 355 | ta367 | Hardware | transceivers manufacturers | port 30 | PASS |  |
| 356 | ta367 | Hardware | transceivers manufacturers | port 28 | PASS |  |
| 357 | ta367 | Hardware | transceivers manufacturers | port 29 | PASS |  |
| 358 | ta367 | Hardware | transceivers manufacturers | port 35 | PASS |  |
| 359 | ta367 | Hardware | transceivers manufacturers | port 34 | PASS |  |
| 360 | ta367 | Hardware | transceivers manufacturers | port 24 | PASS |  |
| 361 | ta367 | Hardware | transceivers manufacturers | port 25 | PASS |  |
| 362 | ta367 | Hardware | transceivers manufacturers | port 26 | PASS |  |
| 363 | ta367 | Hardware | transceivers manufacturers | port 27 | PASS |  |
| 364 | ta367 | Hardware | transceivers manufacturers | port 20 | PASS |  |
| 365 | ta367 | Hardware | transceivers manufacturers | port 21 | PASS |  |
| 366 | ta367 | Hardware | transceivers manufacturers | port 22 | PASS |  |
| 367 | ta367 | Hardware | transceivers manufacturers | port 23 | PASS |  |
| 368 | ta367 | Hardware | transceivers manufacturers | port 46 | PASS |  |
| 369 | ta367 | Hardware | transceivers manufacturers | port 47 | PASS |  |
| 370 | ta367 | Hardware | transceivers manufacturers | port 44 | PASS |  |
| 371 | ta367 | Hardware | transceivers manufacturers | port 45 | PASS |  |
| 372 | ta367 | Hardware | transceivers manufacturers | port 42 | PASS |  |
| 373 | ta367 | Hardware | transceivers manufacturers | port 43 | PASS |  |
| 374 | ta367 | Hardware | transceivers manufacturers | port 40 | PASS |  |
| 375 | ta367 | Hardware | transceivers manufacturers | port 41 | PASS |  |
| 376 | ta367 | Hardware | transceivers manufacturers | port 1 | PASS |  |
| 377 | ta367 | Hardware | transceivers manufacturers | port 3 | PASS |  |
| 378 | ta367 | Hardware | transceivers manufacturers | port 2 | PASS |  |
| 379 | ta367 | Hardware | transceivers manufacturers | port 5 | PASS |  |
| 380 | ta367 | Hardware | transceivers manufacturers | port 4 | PASS |  |
| 381 | ta367 | Hardware | transceivers manufacturers | port 7 | PASS |  |
| 382 | ta367 | Hardware | transceivers manufacturers | port 6 | PASS |  |
| 383 | ta367 | Hardware | transceivers manufacturers | port 9 | PASS |  |
| 384 | ta367 | Hardware | transceivers manufacturers | port 8 | PASS |  |
| 385 | ta367 | Hardware | transceivers manufacturers | port 18 | PASS |  |
| 386 | ta367 | Hardware | transceivers manufacturers | port 13 | PASS |  |
| 387 | ta367 | Hardware | transceivers manufacturers | port 38 | PASS |  |
| 388 | ta367 | Hardware | transceivers manufacturers | port 14 | PASS |  |
| 389 | ta367 | Hardware | transceivers manufacturers | port 11 | PASS |  |
| 390 | ta367 | Hardware | transceivers manufacturers | port 10 | PASS |  |
| 391 | ta367 | Hardware | transceivers manufacturers | port 39 | PASS |  |
| 392 | ta367 | Hardware | transceivers manufacturers | port 12 | PASS |  |
| 393 | ta367 | Hardware | transceivers manufacturers | port 15 | PASS |  |
| 394 | ta367 | Hardware | transceivers manufacturers | port 48 | PASS |  |
| 395 | ta367 | Hardware | transceivers manufacturers | port 17 | PASS |  |
| 396 | ta367 | Hardware | transceivers manufacturers | port 16 | PASS |  |
| 397 | ta367 | Hardware | transceivers manufacturers | port 19 | PASS |  |
| 398 | ta367 | Hardware | transceivers manufacturers | port 54 | PASS |  |
| 399 | ta367 | Hardware | transceivers manufacturers | port 31 | PASS |  |
| 400 | ta367 | Hardware | transceivers manufacturers | port 49 | PASS |  |
| 401 | ta367 | Hardware | transceivers manufacturers | port 51 | PASS |  |
| 402 | ta367 | Hardware | transceivers manufacturers | port 36 | PASS |  |
| 403 | ta367 | Hardware | transceivers manufacturers | port 53 | PASS |  |
| 404 | ta367 | Hardware | transceivers manufacturers | port 52 | PASS |  |
| 405 | ta367 | Hardware | transceivers manufacturers | port 33 | PASS |  |
| 406 | ta367 | Hardware | transceivers manufacturers | port 37 | PASS |  |
| 407 | ta367 | Hardware | transceivers manufacturers | port 32 | PASS |  |
| 408 | ta367 | Hardware | transceivers manufacturers | port 50 | PASS |  |
| 409 | ta366 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 410 | up522 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 411 | ta368 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 412 | smv462 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 413 | ta373 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 414 | cmp308 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 415 | ta367 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 416 | ta366 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet49/1 | PASS |  |
| 417 | ta366 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet50/1 | PASS |  |
| 418 | up522 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2/1 | PASS |  |
| 419 | up522 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3/1 | PASS |  |
| 420 | ta368 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 | PASS |  |
| 421 | ta368 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet49/1 | PASS |  |
| 422 | ta368 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet50/1 | PASS |  |
| 423 | ta368 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet51/1 | PASS |  |
| 424 | ta368 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet52/1 | PASS |  |
| 425 | smv462 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1/1 | PASS |  |
| 426 | smv462 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2/1 | PASS |  |
| 427 | smv462 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3/1 | PASS |  |
| 428 | ta373 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 | PASS |  |
| 429 | ta373 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet50/1 | PASS |  |
| 430 | cmp308 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3/1/1 | PASS |  |
| 431 | cmp308 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3/2/1 | PASS |  |
| 432 | cmp308 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3/3/1 | PASS |  |
| 433 | cmp308 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3/4/1 | PASS |  |
| 434 | cmp308 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3/5/1 | PASS |  |
| 435 | ta367 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet49/1 | PASS |  |
| 436 | ta367 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet50/1 | PASS |  |
| 437 | ta367 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet51/1 | PASS |  |
| 438 | ta366 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet49/1 - remote: cmp308_Ethernet3/2/1 | PASS |  |
| 439 | ta366 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet50/1 - remote: ta368_Ethernet52/1 | PASS |  |
| 440 | up522 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2/1 - remote: ta368_Ethernet2 | PASS |  |
| 441 | up522 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3/1 - remote: ta373_Ethernet2 | PASS |  |
| 442 | ta368 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: up522_Ethernet2/1 | PASS |  |
| 443 | ta368 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet49/1 - remote: ta367_Ethernet51/1 | PASS |  |
| 444 | ta368 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet50/1 - remote: smv462_Ethernet3/1 | PASS |  |
| 445 | ta368 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet51/1 - remote: cmp308_Ethernet3/4/1 | PASS |  |
| 446 | ta368 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet52/1 - remote: ta366_Ethernet50/1 | PASS |  |
| 447 | smv462 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1/1 - remote: cmp308_Ethernet3/1/1 | PASS |  |
| 448 | smv462 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2/1 - remote: ta367_Ethernet49/1 | PASS |  |
| 449 | smv462 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3/1 - remote: ta368_Ethernet50/1 | PASS |  |
| 450 | ta373 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: up522_Ethernet3/1 | PASS |  |
| 451 | ta373 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet50/1 - remote: cmp308_Ethernet3/5/1 | PASS |  |
| 452 | cmp308 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3/1/1 - remote: smv462_Ethernet1/1 | PASS |  |
| 453 | cmp308 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3/2/1 - remote: ta366_Ethernet49/1 | PASS |  |
| 454 | cmp308 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3/3/1 - remote: ta367_Ethernet50/1 | PASS |  |
| 455 | cmp308 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3/4/1 - remote: ta368_Ethernet51/1 | PASS |  |
| 456 | cmp308 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet3/5/1 - remote: ta373_Ethernet50/1 | PASS |  |
| 457 | ta367 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet49/1 - remote: smv462_Ethernet2/1 | PASS |  |
| 458 | ta367 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet50/1 - remote: cmp308_Ethernet3/3/1 | PASS |  |
| 459 | ta367 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet51/1 - remote: ta368_Ethernet49/1 | PASS |  |
| 460 | ta366 | IP Reachability | ip reachability test p2p links | Source: ta366_Ethernet49/1 - Destination: cmp308_Ethernet3/2/1 | PASS |  |
| 461 | ta366 | IP Reachability | ip reachability test p2p links | Source: ta366_Ethernet50/1 - Destination: ta368_Ethernet52/1 | PASS |  |
| 462 | ta368 | IP Reachability | ip reachability test p2p links | Source: ta368_Ethernet49/1 - Destination: ta367_Ethernet51/1 | PASS |  |
| 463 | ta368 | IP Reachability | ip reachability test p2p links | Source: ta368_Ethernet50/1 - Destination: smv462_Ethernet3/1 | PASS |  |
| 464 | ta368 | IP Reachability | ip reachability test p2p links | Source: ta368_Ethernet51/1 - Destination: cmp308_Ethernet3/4/1 | PASS |  |
| 465 | ta368 | IP Reachability | ip reachability test p2p links | Source: ta368_Ethernet52/1 - Destination: ta366_Ethernet50/1 | PASS |  |
| 466 | smv462 | IP Reachability | ip reachability test p2p links | Source: smv462_Ethernet1/1 - Destination: cmp308_Ethernet3/1/1 | PASS |  |
| 467 | smv462 | IP Reachability | ip reachability test p2p links | Source: smv462_Ethernet2/1 - Destination: ta367_Ethernet49/1 | PASS |  |
| 468 | smv462 | IP Reachability | ip reachability test p2p links | Source: smv462_Ethernet3/1 - Destination: ta368_Ethernet50/1 | PASS |  |
| 469 | ta373 | IP Reachability | ip reachability test p2p links | Source: ta373_Ethernet50/1 - Destination: cmp308_Ethernet3/5/1 | PASS |  |
| 470 | cmp308 | IP Reachability | ip reachability test p2p links | Source: cmp308_Ethernet3/1/1 - Destination: smv462_Ethernet1/1 | PASS |  |
| 471 | cmp308 | IP Reachability | ip reachability test p2p links | Source: cmp308_Ethernet3/2/1 - Destination: ta366_Ethernet49/1 | PASS |  |
| 472 | cmp308 | IP Reachability | ip reachability test p2p links | Source: cmp308_Ethernet3/3/1 - Destination: ta367_Ethernet50/1 | PASS |  |
| 473 | cmp308 | IP Reachability | ip reachability test p2p links | Source: cmp308_Ethernet3/4/1 - Destination: ta368_Ethernet51/1 | PASS |  |
| 474 | cmp308 | IP Reachability | ip reachability test p2p links | Source: cmp308_Ethernet3/5/1 - Destination: ta373_Ethernet50/1 | PASS |  |
| 475 | ta367 | IP Reachability | ip reachability test p2p links | Source: ta367_Ethernet49/1 - Destination: smv462_Ethernet2/1 | PASS |  |
| 476 | ta367 | IP Reachability | ip reachability test p2p links | Source: ta367_Ethernet50/1 - Destination: cmp308_Ethernet3/3/1 | PASS |  |
| 477 | ta367 | IP Reachability | ip reachability test p2p links | Source: ta367_Ethernet51/1 - Destination: ta368_Ethernet49/1 | PASS |  |
| 478 | ta366 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 479 | up522 | BGP | ArBGP is configured and operating | ArBGP | FAIL | Operating routing protocol model: ribd |
| 480 | ta368 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 481 | smv462 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 482 | ta373 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 483 | cmp308 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 484 | ta367 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 485 | ta366 | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | PASS |  |
| 486 | up522 | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | PASS |  |
| 487 | ta368 | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | PASS |  |
| 488 | smv462 | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | PASS |  |
| 489 | ta373 | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | PASS |  |
| 490 | cmp308 | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | PASS |  |
| 491 | ta367 | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | PASS |  |
