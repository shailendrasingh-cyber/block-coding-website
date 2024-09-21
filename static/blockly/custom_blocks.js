Blockly.defineBlocksWithJsonArray([{
    "type": "hello_world",
    "message0": "print Hello World",
    "previousStatement": null,
    "nextStatement": null,
    "colour": 160,
    "tooltip": "Prints Hello World",
    "helpUrl": ""
}]);

Blockly.Python['hello_world'] = function(block) {
    return 'print("Hello World")\n';
};
